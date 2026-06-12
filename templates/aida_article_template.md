# Canonical AIDA Article Template — Ambient Lounge Blog

> **Версия:** 2.0 (pixel-perfect по живой статье 2026-06-12)
> **Эталон:** `/blog/idei-dlya-interera/beskarkasnoye-kreslo-dlya-gostinoy/`
> **Формула:** AIDA (Attention → Interest → Desire → Action)
> **Цель:** SEO-топ + конверсия в каталог / заявку

**ОБЯЗАТЕЛЬНО:** каждая статья сайта строится ТОЛЬКО по этому шаблону. Никаких отступлений. Порядок блоков — фиксированный. CSS-значения — точные, менять запрещено.

---

## Структура `detail_text` (полный HTML)

```html
<!-- Обёртка всего detail_text — обязательна -->
<div style="max-width:860px;margin:0 auto;font-family:Georgia,'Times New Roman',serif;color:#1a1a1a;line-height:1.75;font-size:16px;">


<!-- ═══════════════════════════════════════════════════════ -->
<!--  A — ATTENTION  (первый экран, крючок)                 -->
<!-- ═══════════════════════════════════════════════════════ -->

<!-- 1. OPENING QUOTE — эмоциональный хук, первое что видит читатель -->
<blockquote style="border-left:4px solid #c8a96e;margin:0 0 48px;padding:24px 32px;background:#faf8f5;border-radius:0 6px 6px 0;">
  <p style="margin:0;font-size:1.35em;font-style:italic;color:#4a3728;line-height:1.55;">&laquo;<ЭМОЦИОНАЛЬНАЯ ФРАЗА — боль/желание/удивление ЦА. Не рекламная. 1-2 предложения.>&raquo;</p>
</blockquote>

<!-- 2. КРАТКИЙ ОТВЕТ (AEO/AIO — обязателен для featured snippet) -->
<div style="background:#f0ede8;border-radius:8px;padding:24px 28px;margin:0 0 48px;">
  <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#9a8878;">Краткий ответ</p>
  <p style="margin:0;font-size:1.05em;color:#2a2220;line-height:1.65;"><ПРЯМОЙ ОТВЕТ НА ГЛАВНЫЙ ВОПРОС СТАТЬИ — 2-3 предложения. Содержит primary keyword. Самодостаточный фрагмент для AI-ответов.></p>
</div>

<!-- 3. ЛИД — первые 80 слов содержат primary keyword -->
<p style="font-size:1.1em;margin:0 0 1.5em;"><ВХОД В ТЕМУ — контекст, кому адресовано, что узнает читатель.></p>
<p style="font-size:1.1em;margin:0 0 3em;"><ПРОДОЛЖЕНИЕ ЛИДА — мотивация читать дальше.></p>


<!-- ═══════════════════════════════════════════════════════ -->
<!--  I — INTEREST  (вовлечение, снятие возражений)         -->
<!-- ═══════════════════════════════════════════════════════ -->

<!-- H2 SECTION 1: мифы / возражения / «почему это работает» -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:12px;border-bottom:2px solid #e8e3db;"><ЗАГОЛОВОК — провокация, цифра или снятие главного мифа></h2>

<!-- INLINE IMAGE + ТЕКСТ (flex: фото слева, текст справа) -->
<div style="display:flex;gap:28px;align-items:flex-start;margin:0 0 32px;flex-wrap:wrap;">
  <div style="flex:1;min-width:240px;max-width:340px;">
    <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-inline-1.jpg" alt="<ALT — модель + ткань + сценарий>" style="width:100%;border-radius:6px;display:block;box-shadow:0 4px 16px rgba(0,0,0,.09);" loading="lazy">
    <p style="margin:8px 0 0;font-size:12px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;"><ПОДПИСЬ — модель, ткань></p>
  </div>
  <div style="flex:1.4;min-width:260px;">
    <p style="margin:0 0 1.2em;"><strong>Миф 1: «...».</strong> Опровержение — 2-3 предложения.</p>
    <p style="margin:0 0 1.2em;"><strong>Миф 2: «...».</strong> Опровержение.</p>
    <p style="margin:0 0 1.2em;"><strong>Миф 3: «...».</strong> Опровержение.</p>
    <p style="margin:0 0 1.2em;"><strong>Миф 4: «...».</strong> Опровержение.</p>
    <p style="margin:0;"><strong>Миф 5: «...».</strong> Опровержение.</p>
  </div>
</div>

<!-- H2 SECTION 2: сценарии использования / «кому подойдёт» -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 28px;padding-bottom:12px;border-bottom:2px solid #e8e3db;"><ЗАГОЛОВОК — сценарии использования или способы расстановки></h2>

<!-- HERO / INLINE IMAGE с подписью перед сценариями (опционально) -->
<div style="margin:0 0 32px;">
  <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-scene.jpg" alt="<ALT>" style="width:100%;border-radius:6px;display:block;box-shadow:0 4px 20px rgba(0,0,0,.1);" loading="lazy">
  <p style="margin:8px 0 0;font-size:12px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;"><ПОДПИСЬ к фото></p>
</div>

<!-- SCENARIO CARDS — 3 карточки, flex-row, цвет заголовка #c8a96e -->
<div style="display:flex;gap:24px;margin:0 0 40px;flex-wrap:wrap;">
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 1</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;"><ЗАГОЛОВОК СЦЕНАРИЯ></p>
    <p style="margin:0;font-size:.95em;color:#3a3328;"><ОПИСАНИЕ — конкретный, жизненный, 2-3 предложения.></p>
  </div>
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 2</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;"><ЗАГОЛОВОК СЦЕНАРИЯ></p>
    <p style="margin:0;font-size:.95em;color:#3a3328;"><ОПИСАНИЕ></p>
  </div>
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 3</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;"><ЗАГОЛОВОК СЦЕНАРИЯ></p>
    <p style="margin:0;font-size:.95em;color:#3a3328;"><ОПИСАНИЕ></p>
  </div>
</div>

<!-- MID-ARTICLE PULL QUOTE — ключевая мысль раздела -->
<blockquote style="border-left:4px solid #c8a96e;margin:0 0 48px;padding:20px 28px;background:#faf8f5;border-radius:0 6px 6px 0;">
  <p style="margin:0;font-size:1.2em;font-style:italic;color:#4a3728;line-height:1.55;">&laquo;<КОРОТКАЯ СИЛЬНАЯ МЫСЛЬ — резюме раздела или принцип выбора. 1-2 предложения.>&raquo;</p>
</blockquote>


<!-- ═══════════════════════════════════════════════════════ -->
<!--  D — DESIRE  (хочу именно это)                         -->
<!-- ═══════════════════════════════════════════════════════ -->

<!-- H2: PRODUCT CARDS — обязательный раздел, минимум 3 модели -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:12px;border-bottom:2px solid #e8e3db;"><N> моделей для <СЦЕНАРИЙ>: найдите своё</h2>

<!--
  PRODUCT CARD — повторить для каждой модели (3–5 штук).
  ОБЯЗАТЕЛЬНО:
    • цвет хедера — разный для каждой карточки (из палитры ниже)
    • фото — class="lazyload" + data-src (НЕ src)
    • info-box — всегда
    • кнопка «в каталоге» — всегда
  Палитра хедеров (варьировать): #2a4a3f | #1d4571 | #7a3528 | #5a4a3a | #4a2a3e | #2a2220 | #1a3a4a
-->
<div style="margin:0 0 48px;border:1px solid #e8e3db;border-radius:8px;overflow:hidden;">
  <div style="background:<HEADER_COLOR>;padding:16px 24px;">
    <p style="margin:0;font-family:Arial,sans-serif;font-weight:700;font-size:1.1em;color:#fff;letter-spacing:.03em;"><МОДЕЛЬ> — <хук 4-7 слов, выгода для ЦА></p>
  </div>
  <div style="display:flex;gap:0;flex-wrap:wrap;">
    <div style="flex:1;min-width:240px;max-width:340px;">
      <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-<model-id>.jpg" alt="<МОДЕЛЬ> <ТКАНЬ> — бескаркасная мебель Ambient Lounge" loading="lazy" style="width:100%;aspect-ratio:1/1;object-fit:cover;display:block;">
      <p style="margin:8px 0 0;font-size:12px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;text-align:center;padding:0 8px 8px;"><МОДЕЛЬ>, <ТКАНЬ> (<КОЛЛЕКЦИЯ>)</p>
    </div>
    <div style="flex:2;min-width:260px;padding:22px 26px;">
      <p style="margin:0 0 1em;line-height:1.65;"><ОПИСАНИЕ 1 — УТП модели, ощущение, сценарий. 2-3 предложения.></p>
      <p style="margin:0 0 1.2em;line-height:1.65;"><ОПИСАНИЕ 2 — для кого идеально, почему именно эта модель.></p>
      <!-- INFO-BOX — всегда присутствует -->
      <div style="background:#fbf9f5;border-radius:4px;padding:12px 14px;font-family:Arial,sans-serif;font-size:13px;line-height:1.55;">
        <strong>Ткань на фото:</strong> <ТКАНЬ — 1 слово + ключевое свойство><br>
        <strong>Наполнитель:</strong> <Hi-Lux / So-Lux — 1 строка><br>
        <strong>Для кого:</strong> <1 строка — конкретный сегмент ЦА>
      </div>
      <!-- CTA BUTTON — обязателен, без исключений -->
      <div style="text-align:center;margin:16px 0 0;">
        <a href="/<URL-МОДЕЛИ>/" style="display:inline-block;border:2px solid #2a2220;color:#2a2220;font-family:Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:10px 22px;border-radius:3px;text-decoration:none;"><МОДЕЛЬ> в каталоге</a>
      </div>
    </div>
  </div>
</div>
<!-- / конец одной карточки — повторить для следующих моделей -->


<!-- COMPARISON TABLE — обязательна при 2+ моделях/тканях/вариантах -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:12px;border-bottom:2px solid #e8e3db;">Сравнение: <ВАРИАНТ A> против <ВАРИАНТ B></h2>
<p style="margin:0 0 1.5em;"><ВВОДНЫЙ АБЗАЦ перед таблицей — 1-2 предложения.></p>
<div style="overflow-x:auto;margin:0 0 40px;">
<table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px;">
  <thead>
    <tr style="background:#2a2220;color:#fff;">
      <th style="padding:14px 18px;text-align:left;font-weight:600;">Параметр</th>
      <th style="padding:14px 18px;text-align:left;font-weight:600;"><ВАРИАНТ A></th>
      <th style="padding:14px 18px;text-align:left;font-weight:600;"><ВАРИАНТ B></th>
    </tr>
  </thead>
  <tbody>
    <!-- Строки чередовать: background:#faf8f5 / без background -->
    <tr style="background:#faf8f5;">
      <td style="padding:12px 18px;font-weight:600;border-bottom:1px solid #e8e3db;"><ПАРАМЕТР></td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ A></td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ B></td>
    </tr>
    <tr>
      <td style="padding:12px 18px;font-weight:600;border-bottom:1px solid #e8e3db;"><ПАРАМЕТР></td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ A></td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ B></td>
    </tr>
    <!-- последняя строка — без border-bottom -->
    <tr>
      <td style="padding:12px 18px;font-weight:600;"><ПАРАМЕТР></td>
      <td style="padding:12px 18px;"><ЗНАЧЕНИЕ A></td>
      <td style="padding:12px 18px;"><ЗНАЧЕНИЕ B></td>
    </tr>
  </tbody>
</table>
</div>

<!-- CHECKLIST — «чек-лист перед покупкой», 2-колоночный flex-grid -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:12px;border-bottom:2px solid #e8e3db;">Чек-лист перед покупкой</h2>
<div style="display:flex;gap:24px;flex-wrap:wrap;margin:0 0 48px;">
  <!-- Левая колонка: 3 пункта -->
  <div style="flex:1;min-width:240px;">
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 1>.</strong> <ПОЯСНЕНИЕ — конкретное, со значениями.></p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 2>.</strong> <ПОЯСНЕНИЕ.></p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 3>.</strong> <ПОЯСНЕНИЕ.></p>
    </div>
  </div>
  <!-- Правая колонка: 3 пункта -->
  <div style="flex:1;min-width:240px;">
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 4>.</strong> <ПОЯСНЕНИЕ.></p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 5>.</strong> <ПОЯСНЕНИЕ.></p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong><ПАРАМЕТР 6>.</strong> <ПОЯСНЕНИЕ.></p>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════════════════════════════ -->
<!--  A — ACTION  (конверсия)                               -->
<!-- ═══════════════════════════════════════════════════════ -->

<!-- FAQ — 5-8 вопросов, снятие финальных возражений -->
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 24px;padding-bottom:12px;border-bottom:2px solid #e8e3db;">Часто задаваемые вопросы</h2>

<!-- FAQ-блок (повторить 5-8 раз; последний — margin:0 0 48px вместо 16px) -->
<div style="margin:0 0 16px;border:1px solid #e8e3db;border-radius:6px;overflow:hidden;">
  <div style="background:#f5f2ee;padding:14px 20px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;"><ВОПРОС — формулировка как у пользователя в Яндексе></div>
  <div style="padding:14px 20px;font-size:.95em;line-height:1.65;"><ОТВЕТ — прямой, 2-4 предложения. Для AEO — самодостаточный фрагмент без контекста статьи.></div>
</div>
<!-- последний FAQ-блок: -->
<div style="margin:0 0 48px;border:1px solid #e8e3db;border-radius:6px;overflow:hidden;">
  <div style="background:#f5f2ee;padding:14px 20px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;"><ВОПРОС></div>
  <div style="padding:14px 20px;font-size:.95em;line-height:1.65;"><ОТВЕТ></div>
</div>

<!-- MAIN CTA BLOCK — тёмный градиент + золотая кнопка -->
<div style="background:linear-gradient(135deg,#2a2220 0%,#4a3728 100%);border-radius:8px;padding:36px 40px;text-align:center;margin:0 0 16px;">
  <p style="margin:0 0 12px;font-family:Arial,sans-serif;font-size:1.2em;font-weight:700;color:#fff;letter-spacing:.03em;"><ЗАГОЛОВОК CTA — выгода/следующий шаг. Не «Купить», а польза.></p>
  <p style="margin:0 0 24px;font-family:Arial,sans-serif;font-size:.95em;color:#d4c9be;line-height:1.5;"><ПОДЗАГОЛОВОК — 1-2 строки. Снятие последнего сомнения или персонализация.></p>
  <a href="/<РАЗДЕЛ-КАТАЛОГА>/" style="display:inline-block;background:#c8a96e;color:#fff;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;padding:14px 32px;border-radius:4px;text-decoration:none;letter-spacing:.05em;"><ТЕКСТ КНОПКИ — глагол + объект></a>
</div>

<!-- СВЯЗАННЫЕ МАТЕРИАЛЫ -->
<div class="al-blog-products" style="margin:48px 0 0;padding:24px;background:#f8f5f0;border-radius:8px;">
  <h3 style="margin:0 0 16px;font-size:18px;color:#1a1a1a;">Смотрите также</h3>
  <ul style="margin:0;padding:0;list-style:none;">
    <li style="margin:0 0 10px;"><a href="/blog/<SLUG1>/" style="color:#c8a96e;font-weight:500;">→ <ЗАГОЛОВОК СТАТЬИ 1></a></li>
    <li style="margin:0 0 10px;"><a href="/blog/<SLUG2>/" style="color:#c8a96e;font-weight:500;">→ <ЗАГОЛОВОК СТАТЬИ 2></a></li>
    <li style="margin:0 0 10px;"><a href="/<РАЗДЕЛ-КАТАЛОГА>/" style="color:#c8a96e;font-weight:500;">→ Перейти в каталог <КАТЕГОРИЯ></a></li>
  </ul>
</div>

<!-- SCHEMA.ORG — ОБЯЗАТЕЛЬНО в конце detail_text, оба блока -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "<H1 статьи>",
  "description": "<META_DESCRIPTION — 150-160 символов>",
  "url": "https://ambientlounge.ru/blog/<SECTION>/<SLUG>/",
  "datePublished": "<YYYY-MM-DD>",
  "dateModified": "<YYYY-MM-DD>",
  "image": "https://ambientlounge.ru/upload/al_seo_aio/<SLUG>-cover.jpg",
  "author": {"@type": "Organization", "name": "Ambient Lounge", "url": "https://ambientlounge.ru"},
  "publisher": {
    "@type": "Organization",
    "name": "Ambient Lounge",
    "url": "https://ambientlounge.ru",
    "logo": {"@type": "ImageObject", "url": "https://ambientlounge.ru/bitrix/templates/aspro-premier/images/logo.svg"}
  },
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://ambientlounge.ru/blog/<SECTION>/<SLUG>/"}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "<ВОПРОС 1>", "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 1>"}},
    {"@type": "Question", "name": "<ВОПРОС 2>", "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 2>"}},
    {"@type": "Question", "name": "<ВОПРОС 3>", "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 3>"}},
    {"@type": "Question", "name": "<ВОПРОС 4>", "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 4>"}},
    {"@type": "Question", "name": "<ВОПРОС 5>", "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 5>"}}
  ]
}
</script>

</div>
<!-- / конец обёртки detail_text -->
```

---

## Блок-словарь: точный HTML каждого компонента

Ниже — **изолированные блоки** для использования при редактировании старых статей или точечной вставке.

### 1. Цитата / Blockquote (открывающая)

```html
<blockquote style="border-left:4px solid #c8a96e;margin:0 0 48px;padding:24px 32px;background:#faf8f5;border-radius:0 6px 6px 0;">
  <p style="margin:0;font-size:1.35em;font-style:italic;color:#4a3728;line-height:1.55;">&laquo;ТЕКСТ ЦИТАТЫ&raquo;</p>
</blockquote>
```

### 2. Цитата / Pull quote (mid-article, чуть меньше)

```html
<blockquote style="border-left:4px solid #c8a96e;margin:0 0 48px;padding:20px 28px;background:#faf8f5;border-radius:0 6px 6px 0;">
  <p style="margin:0;font-size:1.2em;font-style:italic;color:#4a3728;line-height:1.55;">&laquo;КЛЮЧЕВАЯ МЫСЛЬ РАЗДЕЛА&raquo;</p>
</blockquote>
```

### 3. Краткий ответ (AEO-блок)

```html
<div style="background:#f0ede8;border-radius:8px;padding:24px 28px;margin:0 0 48px;">
  <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#9a8878;">Краткий ответ</p>
  <p style="margin:0;font-size:1.05em;color:#2a2220;line-height:1.65;">ОТВЕТ НА ГЛАВНЫЙ ВОПРОС СТАТЬИ</p>
</div>
```

### 4. H2 заголовок раздела

```html
<h2 style="font-family:Arial,sans-serif;font-size:1.5em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:12px;border-bottom:2px solid #e8e3db;">ЗАГОЛОВОК</h2>
```

*(перед продуктовыми карточками: `margin:0 0 28px`)*

### 5. Карточки сценариев (3 плитки)

```html
<div style="display:flex;gap:24px;margin:0 0 40px;flex-wrap:wrap;">
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 1</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;">ЗАГОЛОВОК</p>
    <p style="margin:0;font-size:.95em;color:#3a3328;">ОПИСАНИЕ</p>
  </div>
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 2</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;">ЗАГОЛОВОК</p>
    <p style="margin:0;font-size:.95em;color:#3a3328;">ОПИСАНИЕ</p>
  </div>
  <div style="flex:1;min-width:220px;background:#faf8f5;border-radius:8px;padding:20px 22px;">
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:#c8a96e;">Сценарий 3</p>
    <p style="margin:0 0 8px;font-size:1.05em;font-weight:700;">ЗАГОЛОВОК</p>
    <p style="margin:0;font-size:.95em;color:#3a3328;">ОПИСАНИЕ</p>
  </div>
</div>
```

### 6. Карточка товара / модели

```html
<div style="margin:0 0 48px;border:1px solid #e8e3db;border-radius:8px;overflow:hidden;">
  <div style="background:#2a4a3f;padding:16px 24px;">
    <!-- Цвет хедера варьировать: #2a4a3f | #1d4571 | #7a3528 | #5a4a3a | #4a2a3e | #2a2220 | #1a3a4a -->
    <p style="margin:0;font-family:Arial,sans-serif;font-weight:700;font-size:1.1em;color:#fff;letter-spacing:.03em;">МОДЕЛЬ — хук 4-7 слов</p>
  </div>
  <div style="display:flex;gap:0;flex-wrap:wrap;">
    <div style="flex:1;min-width:240px;max-width:340px;">
      <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/SLUG-model.jpg" alt="ALT" loading="lazy" style="width:100%;aspect-ratio:1/1;object-fit:cover;display:block;">
      <p style="margin:8px 0 0;font-size:12px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;text-align:center;padding:0 8px 8px;">МОДЕЛЬ, ТКАНЬ</p>
    </div>
    <div style="flex:2;min-width:260px;padding:22px 26px;">
      <p style="margin:0 0 1em;line-height:1.65;">ОПИСАНИЕ 1</p>
      <p style="margin:0 0 1.2em;line-height:1.65;">ОПИСАНИЕ 2</p>
      <div style="background:#fbf9f5;border-radius:4px;padding:12px 14px;font-family:Arial,sans-serif;font-size:13px;line-height:1.55;">
        <strong>Ткань на фото:</strong> ТКАНЬ<br>
        <strong>Наполнитель:</strong> Hi-Lux / So-Lux<br>
        <strong>Для кого:</strong> СЕГМЕНТ ЦА
      </div>
      <div style="text-align:center;margin:16px 0 0;">
        <a href="/URL-МОДЕЛИ/" style="display:inline-block;border:2px solid #2a2220;color:#2a2220;font-family:Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:10px 22px;border-radius:3px;text-decoration:none;">МОДЕЛЬ в каталоге</a>
      </div>
    </div>
  </div>
</div>
```

### 7. Таблица сравнения

```html
<div style="overflow-x:auto;margin:0 0 40px;">
<table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px;">
  <thead>
    <tr style="background:#2a2220;color:#fff;">
      <th style="padding:14px 18px;text-align:left;font-weight:600;">Параметр</th>
      <th style="padding:14px 18px;text-align:left;font-weight:600;">ВАРИАНТ A</th>
      <th style="padding:14px 18px;text-align:left;font-weight:600;">ВАРИАНТ B</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#faf8f5;">
      <td style="padding:12px 18px;font-weight:600;border-bottom:1px solid #e8e3db;">ПАРАМЕТР</td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;">ЗНАЧЕНИЕ A</td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;">ЗНАЧЕНИЕ B</td>
    </tr>
    <tr>
      <td style="padding:12px 18px;font-weight:600;border-bottom:1px solid #e8e3db;">ПАРАМЕТР</td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;">ЗНАЧЕНИЕ A</td>
      <td style="padding:12px 18px;border-bottom:1px solid #e8e3db;">ЗНАЧЕНИЕ B</td>
    </tr>
    <!-- последняя строка без border-bottom -->
    <tr>
      <td style="padding:12px 18px;font-weight:600;">ПАРАМЕТР</td>
      <td style="padding:12px 18px;">ЗНАЧЕНИЕ A</td>
      <td style="padding:12px 18px;">ЗНАЧЕНИЕ B</td>
    </tr>
  </tbody>
</table>
</div>
```

### 8. Чек-лист (2-колоночный)

```html
<div style="display:flex;gap:24px;flex-wrap:wrap;margin:0 0 48px;">
  <div style="flex:1;min-width:240px;">
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
  </div>
  <div style="flex:1;min-width:240px;">
    <!-- аналогичная структура для правой колонки -->
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 16px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
    <div style="display:flex;align-items:flex-start;gap:12px;">
      <span style="font-size:1.3em;line-height:1;margin-top:2px;">&#10003;</span>
      <p style="margin:0;"><strong>ПАРАМЕТР.</strong> ПОЯСНЕНИЕ</p>
    </div>
  </div>
</div>
```

### 9. FAQ-блок

```html
<!-- Все кроме последнего: margin:0 0 16px -->
<div style="margin:0 0 16px;border:1px solid #e8e3db;border-radius:6px;overflow:hidden;">
  <div style="background:#f5f2ee;padding:14px 20px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;">ВОПРОС?</div>
  <div style="padding:14px 20px;font-size:.95em;line-height:1.65;">ОТВЕТ</div>
</div>
<!-- Последний FAQ-блок: margin:0 0 48px -->
<div style="margin:0 0 48px;border:1px solid #e8e3db;border-radius:6px;overflow:hidden;">
  <div style="background:#f5f2ee;padding:14px 20px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;">ВОПРОС?</div>
  <div style="padding:14px 20px;font-size:.95em;line-height:1.65;">ОТВЕТ</div>
</div>
```

### 10. CTA-блок (главный конверсионный)

```html
<div style="background:linear-gradient(135deg,#2a2220 0%,#4a3728 100%);border-radius:8px;padding:36px 40px;text-align:center;margin:0 0 16px;">
  <p style="margin:0 0 12px;font-family:Arial,sans-serif;font-size:1.2em;font-weight:700;color:#fff;letter-spacing:.03em;">ЗАГОЛОВОК CTA</p>
  <p style="margin:0 0 24px;font-family:Arial,sans-serif;font-size:.95em;color:#d4c9be;line-height:1.5;">ПОДЗАГОЛОВОК — снятие последнего сомнения</p>
  <a href="/РАЗДЕЛ/" style="display:inline-block;background:#c8a96e;color:#fff;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;padding:14px 32px;border-radius:4px;text-decoration:none;letter-spacing:.05em;">ТЕКСТ КНОПКИ</a>
</div>
```

### 11. Блок «Смотрите также»

```html
<div class="al-blog-products" style="margin:48px 0 0;padding:24px;background:#f8f5f0;border-radius:8px;">
  <h3 style="margin:0 0 16px;font-size:18px;color:#1a1a1a;">Смотрите также</h3>
  <ul style="margin:0;padding:0;list-style:none;">
    <li style="margin:0 0 10px;"><a href="/blog/SLUG/" style="color:#c8a96e;font-weight:500;">→ ЗАГОЛОВОК СТАТЬИ</a></li>
    <li style="margin:0 0 10px;"><a href="/blog/SLUG/" style="color:#c8a96e;font-weight:500;">→ ЗАГОЛОВОК СТАТЬИ</a></li>
    <li style="margin:0 0 10px;"><a href="/КАТАЛОГ/" style="color:#c8a96e;font-weight:500;">→ Перейти в каталог КАТЕГОРИЯ</a></li>
  </ul>
</div>
```

---

## AIDA: чек-лист перед финальной выдачей

### A — Attention (первый экран)
- [ ] Opening blockquote — эмоциональный, не рекламный
- [ ] Краткий ответ — прямой, содержит primary keyword, самодостаточный
- [ ] Лид-параграфы — primary keyword в первых 80 словах

### I — Interest (вовлечение)
- [ ] Минимум 2 H2-секции до product cards
- [ ] Снятие возражений / мифов — конкретные, с фактами
- [ ] Минимум 2 фото с alt и подписями
- [ ] Scenario cards (3 плитки) — конкретные жизненные ситуации
- [ ] Mid-article pull quote — резюме раздела

### D — Desire (хочу это купить)
- [ ] Минимум 3 product cards (оптимально 4-5)
- [ ] Каждая карточка: фото + 2 описания + info-box + кнопка «в каталоге»
- [ ] Цвета хедеров карточек — разные (из палитры)
- [ ] Таблица сравнения (не менее 5 строк)
- [ ] Чек-лист перед покупкой (6 пунктов, 2 колонки)

### A — Action (конверсия)
- [ ] FAQ: 5-8 вопросов, последний с margin 48px
- [ ] CTA-блок: тёмный градиент (#2a2220→#4a3728) + золотая кнопка (#c8a96e)
- [ ] Кнопка CTA: глагол + объект, не «Купить»
- [ ] Блок «Смотрите также»: 2 статьи + 1 ссылка в каталог
- [ ] 2 Schema.org LD+JSON: Article + FAQPage — в конце detail_text
- [ ] Нуль плейсхолдеров `[ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ]` в финальном HTML

---

## Обязательные технические требования

| Параметр | Требование |
|----------|-----------|
| Длина | 2000–3500 слов |
| Фото | ≥ 3 с `class="lazyload"` + `data-src=` (НЕ `src=`) + осмысленным `alt` |
| Внутренние ссылки | ≥ 4 (каталог + другие статьи) |
| Product cards | ≥ 3, каждая с кнопкой «в каталоге» |
| FAQ | 5–8 вопросов |
| Schema | Article + FAQPage (LD+JSON), в конце detail_text |
| Плейсхолдеры | Нуль — никаких `[ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ]` |
| META_TITLE | ≤ 70 символов |
| META_DESCRIPTION | 150–160 символов |
| Путь изображений | `/upload/al_seo_aio/<slug>-*.jpg` |

---

## Запрещено

- `<h3>` + `<p>` + «- список через тире» для секций моделей — только карточки
- Schema.org как видимый текст в теле статьи
- `[ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ]` / `[ГИПОТЕЗА]` в финальном HTML
- Прямые URL Яндекс.Диска или внешних CDN в `src=` у изображений
- Одинаковый цвет хедеров у всех карточек
- Отсутствие кнопки в любой product card
- `loading="eager"` — только `loading="lazy"` + `class="lazyload"` + `data-src=`

---

## Цветовая система бренда

| Назначение | CSS-значение |
|-----------|-------------|
| Opening blockquote фон | `#faf8f5` |
| Opening blockquote акцент | `border-left: 4px solid #c8a96e` |
| Opening blockquote текст | `color:#4a3728` |
| Краткий ответ фон | `#f0ede8` |
| Краткий ответ лейбл | `color:#9a8878` |
| Краткий ответ текст | `color:#2a2220` |
| Сценарии фон плитки | `#faf8f5` |
| Сценарии лейбл «Сценарий N» | `color:#c8a96e` |
| Сценарии текст | `color:#3a3328` |
| H2 border-bottom | `2px solid #e8e3db` |
| Table header | `background:#2a2220; color:#fff` |
| Table row alt | `background:#faf8f5` |
| Table border | `1px solid #e8e3db` |
| Info-box фон | `#fbf9f5` |
| FAQ вопрос фон | `#f5f2ee` |
| CTA градиент | `linear-gradient(135deg,#2a2220 0%,#4a3728 100%)` |
| CTA подзаголовок | `color:#d4c9be` |
| Кнопка outline | `border:2px solid #2a2220; color:#2a2220` |
| Кнопка filled (CTA) | `background:#c8a96e; color:#fff` |
| «Смотрите также» фон | `#f8f5f0` |
| Ссылки в footer-блоке | `color:#c8a96e` |

**Хедеры карточек товаров** (варьировать, не повторять в одной статье):
`#2a4a3f` (зелёный) · `#1d4571` (синий) · `#7a3528` (винный) · `#5a4a3a` (коричневый) · `#4a2a3e` (бордо) · `#2a2220` (тёмный) · `#1a3a4a` (сине-зелёный)
