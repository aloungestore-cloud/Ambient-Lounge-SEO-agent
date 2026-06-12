# Canonical AIDA Article Template — Ambient Lounge Blog

> **Версия:** 1.0 (утверждена пользователем 2026-06-12)  
> **Эталон:** `/blog/idei-dlya-interera/beskarkasnoye-kreslo-dlya-gostinoy/`  
> **Формула:** AIDA (Attention → Interest → Desire → Action)  
> **Цель:** SEO-топ + конверсия в каталог / заявку

**ОБЯЗАТЕЛЬНО:** каждая статья сайта строится ТОЛЬКО по этому шаблону. Никаких отступлений. Порядок блоков — фиксированный.

---

## Структура `detail_text` (полный HTML)

```html
<!-- ═══════════════════════════════════════════════ -->
<!--  A — ATTENTION  (первый экран, крючок)          -->
<!-- ═══════════════════════════════════════════════ -->

<!-- 1. OPENING QUOTE — эмоциональный хук -->
<blockquote style="border-left:4px solid #c8a96e;margin:0 0 40px;padding:20px 28px;background:#faf8f5;border-radius:0 6px 6px 0;">
  <p style="margin:0;font-size:1.25em;font-style:italic;color:#4a3728;line-height:1.55;">&laquo;<ЭМОЦИОНАЛЬНАЯ ФРАЗА — боль/желание/удивление ЦА>&raquo;</p>
</blockquote>

<!-- 2. КРАТКИЙ ОТВЕТ (AEO/AIO — обязателен) -->
<div style="background:#f0ede8;border-radius:8px;padding:20px 24px;margin:0 0 40px;">
  <p style="margin:0 0 6px;font-family:Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#9a8878;">Краткий ответ</p>
  <p style="margin:0;font-size:1.05em;color:#2a2220;line-height:1.65;"><ПРЯМОЙ ОТВЕТ НА ГЛАВНЫЙ ВОПРОС СТАТЬИ — 2-3 предложения. Содержит primary keyword.></p>
</div>

<!-- 3. LEAD — лид-параграф (первые 80 слов содержат primary keyword) -->
<p style="font-size:1.08em;margin:0 0 1.4em;line-height:1.7;"><ЛЁГКИЙ ВХОД В ТЕМУ — контекст, для кого, что узнает.></p>

<!-- HERO IMAGE — обязателен, loading="eager" для LCP -->
<figure style="margin:0 0 40px;">
  <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-cover.jpg" alt="<ALT — модель + ткань + сценарий>" style="width:100%;border-radius:8px;display:block;box-shadow:0 4px 20px rgba(0,0,0,.08);" loading="lazy">
  <figcaption style="font-size:12px;color:#9a8878;text-align:center;margin-top:8px;font-style:italic;"><ПОДПИСЬ — модель, ткань, сценарий></figcaption>
</figure>


<!-- ═══════════════════════════════════════════════ -->
<!--  I — INTEREST  (вовлечение, снятие возражений) -->
<!-- ═══════════════════════════════════════════════ -->

<!-- H2 SECTION 1: "5 мифов" / "Почему X" / снятие возражений -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:0 0 20px;padding-bottom:10px;border-bottom:2px solid #e8e3db;"><ЗАГОЛОВОК — провокация или раскрытие мифа></h2>

<!-- inline image + caption (flex: image left, text right) -->
<div style="display:flex;gap:28px;align-items:flex-start;margin:0 0 32px;flex-wrap:wrap;">
  <div style="flex:1;min-width:240px;">
    <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-inline-1.jpg" alt="<ALT>" style="width:100%;border-radius:6px;display:block;box-shadow:0 4px 16px rgba(0,0,0,.09);" loading="lazy">
    <p style="margin:6px 0 0;font-size:11px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;"><ПОДПИСЬ></p>
  </div>
  <div style="flex:1.4;min-width:260px;">
    <p style="margin:0 0 1em;"><ТЕКСТ БЛОКА></p>
    <p style="margin:0;"><ПРОДОЛЖЕНИЕ></p>
  </div>
</div>

<!-- H2 SECTION 2: сценарии / «кому подойдёт» / практика -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:48px 0 20px;padding-bottom:10px;border-bottom:2px solid #e8e3db;"><ЗАГОЛОВОК></h2>
<p style="margin:0 0 1.2em;"><ТЕКСТ></p>
<!-- ещё inline image если есть -->


<!-- ═══════════════════════════════════════════════ -->
<!--  D — DESIRE  (хочу именно это)                  -->
<!-- ═══════════════════════════════════════════════ -->

<!-- H2: PRODUCT CARDS — обязательный раздел, 3-5 моделей -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:48px 0 24px;padding-bottom:10px;border-bottom:2px solid #e8e3db;"><N> моделей для <СЦЕНАРИЙ>: найдите своё</h2>

<!-- PRODUCT CARD (повторить для каждой модели, варьировать цвет хедера) -->
<div style="margin:0 0 32px;border:1px solid #e8e3db;border-radius:8px;overflow:hidden;">
  <div style="background:<HEADER_COLOR>;padding:14px 22px;">
    <!-- Палитра хедеров (варьировать): #2a4a3f | #1d4571 | #7a3528 | #5a4a3a | #4a2a3e | #2a2220 | #1a3a4a | #5a6f1f -->
    <p style="margin:0;font-family:Arial,sans-serif;font-weight:700;font-size:1.05em;color:#fff;letter-spacing:.03em;"><МОДЕЛЬ> — <хук 4-7 слов, выгода для ЦА></p>
  </div>
  <div style="display:flex;gap:0;flex-wrap:wrap;">
    <div style="flex:1;min-width:240px;max-width:340px;">
      <img class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="/upload/al_seo_aio/<SLUG>-<model>.jpg" alt="<МОДЕЛЬ> <ТКАНЬ> — <ALT описание>" loading="lazy" style="width:100%;aspect-ratio:1/1;object-fit:cover;display:block;">
      <p style="margin:6px 0 0;font-size:11px;color:#9a8878;font-style:italic;font-family:Arial,sans-serif;text-align:center;padding:0 8px 8px;"><МОДЕЛЬ>, <ТКАНЬ></p>
    </div>
    <div style="flex:2;min-width:260px;padding:22px 26px;">
      <p style="margin:0 0 1em;line-height:1.65;"><ОПИСАНИЕ 1 — УТП модели, ощущение, сценарий.></p>
      <p style="margin:0 0 1.2em;line-height:1.65;"><ОПИСАНИЕ 2 — для кого идеально, почему именно эта модель.></p>
      <!-- INFO-BOX -->
      <div style="background:#fbf9f5;border-radius:4px;padding:12px 14px;font-family:Arial,sans-serif;font-size:13px;line-height:1.55;margin:0 0 0;">
        <strong>Ткань на фото:</strong> <ТКАНЬ — свойство 1 слово><br>
        <strong>Наполнитель:</strong> <Hi-Lux / So-Lux — 1 строка><br>
        <strong>Для кого:</strong> <1 строка — конкретный сегмент ЦА>
      </div>
      <!-- CTA BUTTON — обязателен в каждой карточке -->
      <div style="text-align:center;margin:16px 0 0;">
        <a href="/<URL-МОДЕЛИ>/" style="display:inline-block;border:2px solid #2a2220;color:#2a2220;font-family:Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:10px 22px;border-radius:3px;text-decoration:none;"><МОДЕЛЬ> в каталоге</a>
      </div>
    </div>
  </div>
</div>
<!-- / конец одной карточки — повторить для следующих моделей -->

<!-- COMPARISON TABLE — обязательна если 2+ модели/ткани/варианта -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:48px 0 20px;padding-bottom:10px;border-bottom:2px solid #e8e3db;">Сравнение: <ВАРИАНТ A> против <ВАРИАНТ B></h2>
<div style="overflow-x:auto;margin:0 0 40px;">
<table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px;line-height:1.5;">
  <thead>
    <tr style="background:#2a2220;color:#fff;">
      <th style="padding:13px 16px;text-align:left;font-weight:600;min-width:120px;">Параметр</th>
      <th style="padding:13px 16px;text-align:left;font-weight:600;"><ВАРИАНТ A></th>
      <th style="padding:13px 16px;text-align:left;font-weight:600;"><ВАРИАНТ B></th>
    </tr>
  </thead>
  <tbody>
    <!-- Строки чередовать: #faf8f5 / #fff -->
    <tr style="background:#faf8f5;">
      <td style="padding:11px 16px;font-weight:600;border-bottom:1px solid #e8e3db;"><ПАРАМЕТР></td>
      <td style="padding:11px 16px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ A></td>
      <td style="padding:11px 16px;border-bottom:1px solid #e8e3db;"><ЗНАЧЕНИЕ B></td>
    </tr>
    <!-- ещё 4-6 строк -->
  </tbody>
</table>
</div>

<!-- CHECKLIST — «как выбрать» / «чек-лист перед покупкой» -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:48px 0 20px;padding-bottom:10px;border-bottom:2px solid #e8e3db;">Чек-лист перед покупкой</h2>
<div style="display:flex;gap:20px;flex-wrap:wrap;margin:0 0 40px;">
  <!-- Каждый пункт: -->
  <div style="display:flex;align-items:flex-start;gap:12px;margin:0 0 12px;flex:1;min-width:260px;">
    <span style="font-size:1.2em;line-height:1;margin-top:3px;color:#c8a96e;">✓</span>
    <p style="margin:0;line-height:1.6;"><strong><ПАРАМЕТР>.</strong> <ПОЯСНЕНИЕ — 1-2 предложения.></p>
  </div>
  <!-- Повторить 5-7 раз -->
</div>


<!-- ═══════════════════════════════════════════════ -->
<!--  A — ACTION  (конверсия)                        -->
<!-- ═══════════════════════════════════════════════ -->

<!-- FAQ — 5-8 вопросов, снятие финальных возражений -->
<h2 style="font-family:Arial,sans-serif;font-size:1.45em;font-weight:700;color:#1a1a1a;margin:48px 0 20px;padding-bottom:10px;border-bottom:2px solid #e8e3db;">Часто задаваемые вопросы</h2>
<!-- Один FAQ-блок (повторить 5-8 раз) -->
<div style="margin:0 0 12px;border:1px solid #e8e3db;border-radius:6px;overflow:hidden;">
  <div style="background:#f5f2ee;padding:13px 18px;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;line-height:1.4;"><ВОПРОС — формулировка как у пользователя в Яндексе></div>
  <div style="padding:13px 18px;font-size:.95em;line-height:1.65;"><ОТВЕТ — прямой, 2-4 предложения. Для AEO — самодостаточный фрагмент.></div>
</div>

<!-- MAIN CTA BLOCK — финальный конверсионный блок -->
<div style="background:linear-gradient(135deg,#2a2220 0%,#4a3728 100%);border-radius:8px;padding:32px 36px;text-align:center;margin:48px 0 16px;">
  <p style="margin:0 0 10px;font-family:Arial,sans-serif;font-size:1.15em;font-weight:700;color:#fff;letter-spacing:.02em;"><ЗАГОЛОВОК CTA — выгода/следующий шаг></p>
  <p style="margin:0 0 22px;font-family:Arial,sans-serif;font-size:.9em;color:#d4c9be;line-height:1.55;"><ПОДЗАГОЛОВОК — снятие последнего сомнения, 1-2 строки></p>
  <a href="/<РАЗДЕЛ-КАТАЛОГА>/" style="display:inline-block;background:#c8a96e;color:#fff;font-family:Arial,sans-serif;font-weight:700;font-size:.95em;padding:13px 30px;border-radius:4px;text-decoration:none;letter-spacing:.05em;"><ТЕКСТ КНОПКИ — действие + объект></a>
</div>

<!-- СВЯЗАННЫЕ СТАТЬИ -->
<div class="al-blog-products" style="margin:40px 0 0;padding:22px;background:#f8f5f0;border-radius:8px;">
  <h3 style="margin:0 0 14px;font-size:17px;font-family:Arial,sans-serif;color:#1a1a1a;">Смотрите также</h3>
  <ul style="margin:0;padding:0;list-style:none;">
    <li style="margin:0 0 8px;"><a href="/blog/<SLUG1>/" style="color:#c8a96e;font-weight:500;font-family:Arial,sans-serif;">→ <ЗАГОЛОВОК СТАТЬИ 1></a></li>
    <li style="margin:0 0 8px;"><a href="/blog/<SLUG2>/" style="color:#c8a96e;font-weight:500;font-family:Arial,sans-serif;">→ <ЗАГОЛОВОК СТАТЬИ 2></a></li>
    <li style="margin:0;"><a href="/<РАЗДЕЛ-КАТАЛОГА>/" style="color:#c8a96e;font-weight:500;font-family:Arial,sans-serif;">→ Перейти в каталог <КАТЕГОРИЯ></a></li>
  </ul>
</div>

<!-- SCHEMA.ORG — ОБЯЗАТЕЛЬНО в конце detail_text, два блока -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "<H1 статьи>",
  "description": "<META_DESCRIPTION>",
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
    {
      "@type": "Question",
      "name": "<ВОПРОС 1>",
      "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 1>"}
    },
    {
      "@type": "Question",
      "name": "<ВОПРОС 2>",
      "acceptedAnswer": {"@type": "Answer", "text": "<ОТВЕТ 2>"}
    }
  ]
}
</script>
```

---

## AIDA: чек-лист перед финальной выдачей

### A — Attention (первый экран)
- [ ] Opening quote — эмоциональный хук, не рекламный
- [ ] Краткий ответ — прямой, содержит primary keyword
- [ ] Лид-параграф — primary keyword в первых 80 словах
- [ ] Hero image — `loading="lazy"`, осмысленный alt

### I — Interest (вовлечение)
- [ ] Минимум 2 H2-секции до product cards
- [ ] Снятие возражений / мифов / «почему это работает»
- [ ] Минимум 2 inline-фото с подписями и alt
- [ ] Сценарии использования — конкретные, жизненные

### D — Desire (хочу это купить)
- [ ] Минимум 3 product cards (оптимально 4-5)
- [ ] Каждая карточка: фото + описание + info-box + кнопка «в каталоге»
- [ ] Цвета хедеров карточек — разные (из палитры)
- [ ] Таблица сравнения (модели / ткани / варианты)
- [ ] Чек-лист «как выбрать» / «перед покупкой»

### A — Action (конверсия)
- [ ] FAQ: 5-8 вопросов в формате «вопрос пользователя / прямой ответ»
- [ ] Главный CTA-блок: тёмный градиент + золотая кнопка
- [ ] Текст кнопки: глагол + объект («Смотреть каталог кресел»)
- [ ] Блок «Смотрите также»: 2 статьи + 1 ссылка в каталог
- [ ] 2 Schema.org LD+JSON: Article + FAQPage

---

## Обязательные технические требования

| Параметр | Требование |
|----------|-----------|
| Длина | 2000–3500 слов |
| Inline фото | ≥ 3 (все с `loading="lazy"` + осмысленным alt) |
| Внутренние ссылки | ≥ 4 (каталог + другие статьи) |
| Product cards | ≥ 3, каждая с кнопкой «в каталоге» |
| FAQ | 5–8 вопросов |
| Schema | Article + FAQPage (LD+JSON), в конце detail_text |
| Плейсхолдеры | Нуль — никаких [ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ] |
| META_TITLE | ≤ 70 символов |
| META_DESCRIPTION | 150–160 символов |
| Изображения | `/upload/al_seo_aio/<slug>-*.jpg`, через n8n |

---

## Запрещено

- `h3` + `<p>` + «- список через тире» для секций моделей → только карточки
- Схема напрямую в теле как видимый текст
- `[ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ]` / `[ГИПОТЕЗА]` в финальном HTML
- Прямые URL Яндекс.Диска в `<img src>` — только `/upload/al_seo_aio/`
- Одинаковый цвет хедеров у всех карточек
- Отсутствие кнопки в любой product card

---

## Цветовая палитра бренда

| Назначение | CSS |
|-----------|-----|
| CTA кнопки (outline) | `border:2px solid #2a2220; color:#2a2220` |
| CTA кнопки (filled) | `background:#c8a96e; color:#fff` |
| Финальный CTA-блок | `background:linear-gradient(135deg,#2a2220 0%,#4a3728 100%)` |
| Info-box фон | `#fbf9f5` |
| FAQ вопрос фон | `#f5f2ee` |
| Краткий ответ фон | `#f0ede8` |
| Opening quote фон | `#faf8f5` |
| Смотрите также фон | `#f8f5f0` |
| Ссылки в footer-блоке | `#c8a96e` |
| H2 border-bottom | `2px solid #e8e3db` |
| Table header | `background:#2a2220; color:#fff` |
| Table row alt | `background:#faf8f5` |

**Хедеры карточек** (варьировать):
`#2a4a3f` · `#1d4571` · `#7a3528` · `#5a4a3a` · `#4a2a3e` · `#2a2220` · `#1a3a4a` · `#5a6f1f`
