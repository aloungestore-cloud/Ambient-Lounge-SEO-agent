<?php
/**
 * SEO-AIO: weekly Yandex Metrika "search phrases" export.
 *
 * API: GET https://api-metrika.yandex.net/stat/v1/data
 *   dimensions=ym:s:searchPhrase  metrics=ym:s:visits
 *   filters: ym:s:searchPhrase!n  (non-null)   date1=8daysAgo date2=yesterday
 * Output: /home/bitrix/www/upload/al_seo_aio/metrika-weekly/YYYY-WW.tsv
 *   columns: phrase / visits / theme / week_iso     (theme="" — заполнит движок)
 * Auth: METRIKA_OAUTH_TOKEN + METRIKA_COUNTER_ID from /home/bitrix/cron/al_seo_aio.env
 * Cron: 0 5 * * 0 bitrix /usr/bin/php /home/bitrix/cron/al_metrika_weekly.php
 * Flags: --dry-run  --force
 */
date_default_timezone_set('Europe/Moscow');

$ENV_FILE   = '/home/bitrix/cron/al_seo_aio.env';
$OUTPUT_DIR = '/home/bitrix/www/upload/al_seo_aio/metrika-weekly';
$LOG_FILE   = '/var/log/bitrix/seo_aio_metrika.log';
$LOCK_FILE  = '/var/tmp/al-metrika-weekly.lock';
$API_URL    = 'https://api-metrika.yandex.net/stat/v1/data';
$LIMIT      = 500;

function al_log($m) { global $LOG_FILE;
    $line='['.date('Y-m-d H:i:s').'] '.$m."\n"; @file_put_contents($LOG_FILE,$line,FILE_APPEND); fwrite(STDOUT,$line); }

$args=$argv??[]; $dryRun=in_array('--dry-run',$args,true); $force=in_array('--force',$args,true);

$lock=@fopen($LOCK_FILE,'c');
if($lock===false || !flock($lock,LOCK_EX|LOCK_NB)){ al_log('skip: another instance running'); exit(0); }
@mkdir(dirname($LOG_FILE),0755,true);

if(!is_file($ENV_FILE)){ al_log("error: $ENV_FILE not found"); exit(1); }
$env=[];
foreach(preg_split('/\r?\n/',(string)file_get_contents($ENV_FILE)) as $l){
    $l=trim($l); if($l===''||$l[0]==='#'||strpos($l,'=')===false) continue;
    [$k,$v]=explode('=',$l,2); $env[trim($k)]=trim($v," \t\"'");
}
$token=$env['METRIKA_OAUTH_TOKEN']??''; $counter=$env['METRIKA_COUNTER_ID']??'';
if($token===''||$counter===''){ al_log('skip: METRIKA_OAUTH_TOKEN/COUNTER_ID not set'); exit(0); }

$cutoff=new DateTime('now'); $cutoff->modify('-3 days');
while((int)$cutoff->format('N')!==7){ $cutoff->modify('-1 day'); }
$weekIso=$cutoff->format('o-W');
$outputFile=$OUTPUT_DIR.'/'.$weekIso.'.tsv';
if(!$force && !$dryRun && is_file($outputFile)){ al_log("skip: $outputFile exists (--force)"); exit(0); }

$qs=http_build_query([
    'ids'=>$counter, 'dimensions'=>'ym:s:searchPhrase', 'metrics'=>'ym:s:visits',
    'filters'=>'ym:s:searchPhrase!n', 'date1'=>'8daysAgo', 'date2'=>'yesterday',
    'sort'=>'-ym:s:visits', 'limit'=>$LIMIT,
]);
$ch=curl_init($API_URL.'?'.$qs);
curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,
    CURLOPT_HTTPHEADER=>['Authorization: OAuth '.$token], CURLOPT_TIMEOUT=>60]);
$resp=curl_exec($ch); $code=curl_getinfo($ch,CURLINFO_HTTP_CODE); curl_close($ch);
if($code!==200){ al_log("error: HTTP $code ".substr((string)$resp,0,200)); exit(0); }
$data=json_decode((string)$resp,true);

$rows=[];
foreach(($data['data']??[]) as $item){
    $phrase=trim($item['dimensions'][0]['name']??'');
    $visits=(int)round($item['metrics'][0]??0);
    if($phrase!=='' && $visits>0){ $rows[]=['phrase'=>$phrase,'visits'=>$visits]; }
}
al_log("week=$weekIso rows=".count($rows));

if($dryRun){
    foreach(array_slice($rows,0,5) as $i=>$r){ al_log(sprintf("  %d. '%s' visits=%d",$i+1,$r['phrase'],$r['visits'])); }
    exit(0);
}
if(count($rows)===0){ al_log('no rows — skip write'); exit(0); }

if(!is_dir($OUTPUT_DIR)){ mkdir($OUTPUT_DIR,0755,true); @chown($OUTPUT_DIR,'bitrix'); @chgrp($OUTPUT_DIR,'bitrix'); }
$tmp=$outputFile.'.tmp.'.getmypid(); $fh=@fopen($tmp,'w');
if($fh===false){ al_log("error: cannot write $tmp"); exit(6); }
fwrite($fh,"phrase\tvisits\ttheme\tweek_iso\n");
foreach($rows as $r){ $p=str_replace(["\t","\n","\r"],' ',$r['phrase']); fwrite($fh,"{$p}\t{$r['visits']}\t\t{$weekIso}\n"); }
fclose($fh);
if(!rename($tmp,$outputFile)){ al_log('error: rename failed'); @unlink($tmp); exit(7); }
@chown($outputFile,'bitrix'); @chgrp($outputFile,'bitrix'); @chmod($outputFile,0644);
al_log('wrote '.count($rows).' rows to '.$outputFile);
exit(0);
