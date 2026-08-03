# 📊 FRAME 02 — DASHBOARD

## Purpose
The main landing screen of the Trading Journal app. Surfaces performance at a glance — KPIs, equity curve, recent trades, activity, and trader discipline — while staying consistent with the Frame 01 cover's noir/emerald design system.

---

## 📐 Frame Specifications

| Property | Value |
|---|---|
| Frame Name | 02 - Dashboard |
| Frame Size | Desktop — 1440 × 1024 px |
| Layout | Two-column: fixed Sidebar + fluid Content |
| Background | `#0A0A0A` (Noir) |

---

## 🎨 Design Tokens

### Color
| Token | Hex / Value | Usage |
|---|---|---|
| `bg` | `#0A0A0A` | Frame background |
| `panel` | `#111111` | Default card/panel fill |
| `panel-alt` | `#141414` | Inputs, nav account card, badges |
| `border` | `#232323` | Standard 1px borders |
| `border-soft` | `#1B1B1B` | Subtle dividers, panel outlines |
| `emerald` | `#2E8B57` | Signature brand color — fills, bars, accents |
| `emerald-text` | `#4CAE7C` | Emerald used as text/icon (brighter for legibility) |
| `emerald-soft` | `rgba(46,139,87,0.14)` | Active-state backgrounds, badges |
| `emerald-soft-border` | `rgba(46,139,87,0.35)` | Borders on emerald-tinted elements |
| `red-muted` | `#9A5252` | Negative/loss indicators only (desaturated, not a bright red) |
| `text-primary` | `#FFFFFF` | Headings, values, primary labels |
| `text-secondary` | `#B3B3B3` | Body text, table cells |
| `text-tertiary` | `#6E6E6E` | Captions, muted labels |
| `text-quaternary` | `#4A4A4A` | Section eyebrows, axis labels, faintest text |

### Typography
| Role | Font | Weight | Notes |
|---|---|---|---|
| Page title / KPI values / logo wordmark | Space Grotesk | Bold (700) / SemiBold (600) | Same display face as Frame 01 |
| Body / labels / table text | Inter | Regular–SemiBold (400–600) | |
| Tagline | Inter | Italic Medium (500) | Matches Frame 01 tagline treatment |

### Spacing & Radius
| Token | Value |
|---|---|
| `radius-lg` | 14px — panels, KPI cards |
| `radius-md` | 10px | 
| `radius-sm` | 7px — nav items, buttons, small controls |
| Panel padding | 18px vertical / 20px horizontal |
| Column gutter | 16px between all major panels |
| Content margin | 26px top, 24px bottom, 32px left/right |

### Background
Faint grid overlay across the full frame, consistent with the noir/no-texture rule from Frame 01:
- Two linear-gradients (horizontal + vertical hairlines), `rgba(255,255,255,0.028)`, 1px lines
- Grid cell size: 36 × 36 px

### Bottom Accent
Same treatment as Frame 01: 2px line, full width, `#2E8B57` at 40% opacity, pinned to the absolute bottom of the frame (sits above both sidebar and content).

---

## 🧩 Component 1 — Sidebar

| Property | Value |
|---|---|
| Width | 240px, full height (1024px) |
| Background | `#0C0C0C` |
| Right border | 1px `border-soft` |
| Padding | 28px top, 20px sides/bottom |

**Structure (top to bottom):**
1. **Brand block** — logo (30×30px, the finalized node-arc mark) + wordmark stack (TRADING JOURNAL, Space Grotesk Bold 13.5px, +6% tracking / tagline, Inter Italic Medium 9.5px, `text-tertiary`). Bottom border divider, 22px padding below, 20px margin below that.
2. **"MENU" eyebrow** — 10px, SemiBold, +8% tracking, uppercase, `text-quaternary`
3. **Nav list** — 8 items, 2px gap between:
   - Dashboard
   - Calendar
   - Trades
   - Performance Analysis
   - Journal
   - Rules
   - Risk Manager
   - Settings

   Each item: 16×16px stroke icon + 13px Medium label, 11px gap, 9px/10px padding, `radius-sm` corners.

4. **Spacer** — flexible, pushes account block to bottom
5. **Account card** — 30×30px avatar (emerald gradient circle with initials), name (12px SemiBold white) + role (10.5px `text-tertiary`), in a `panel-alt` bordered card
6. **Version label** — centered, 10px, `text-quaternary` — "Northtrail v1.0"

**Active nav state** (Dashboard):
- Background: `emerald-soft`
- Text: white (vs. `text-secondary` default)
- Icon stroke: `emerald-text`
- 3px emerald tab/accent bar on the far left edge, rounded on the outer corner, vertically centered on the item (16px tall)

---

## 🧩 Component 2 — Top Bar

| Element | Spec |
|---|---|
| Page title | "Dashboard" — Space Grotesk SemiBold, 22px, white |
| Search field | 260px wide pill, `panel-alt` fill, 1px `border`, search icon (14px) + placeholder "Search trades, symbols...", 12.5px Inter |
| Notification icon | 34px circle button, `panel-alt` fill, bell icon (15px), small emerald status dot top-right |
| Avatar control | 34px circle, emerald gradient fill, initials, 12px SemiBold |

Layout: flex row, space-between, title left / search + icons right, 12px gap between right-side controls. 22px margin below the whole bar.

---

## 🧩 Component 3 — KPI Row

Four equal-width cards in a single row, 16px gutter, 18px margin below.

**Card anatomy** (applies to all 4):
- Panel styling: `panel` fill, `border-soft` outline, `radius-lg`, 16px/18px padding
- Label: 11px SemiBold uppercase, +6% tracking, `text-tertiary`
- Value: Space Grotesk Bold, 25px, white
- Change indicator: small arrow icon (11px) + bold 11.5px value + regular "this month" note in `text-tertiary`
  - Positive → `emerald-text` + up arrow
  - Negative → `red-muted` + down arrow

**Card content:**
| Card | Value | Change |
|---|---|---|
| Total Profit | $24,582.30 | ▲ +12.4% this month |
| Win Rate | 68.4% | ▲ +3.2% this month |
| Profit Factor | 2.14 | ▼ −0.08 this month |
| Trades | 142 | ▲ +18 this month |

---

## 🧩 Component 4 — Equity Curve Panel

Largest panel in the layout — occupies ~64% width of the main content row.

- **Header row:** "Equity Curve" title (14px SemiBold) + timeframe toggle, right-aligned
  - Toggle: pill container (`panel-alt`, `border-soft`, full radius), options `1W 1M 3M 1Y ALL`, active state = `emerald-soft` background + `emerald-text`
- **Chart:** SVG line + area chart
  - Line: 2.5px stroke, `emerald-text`, rounded caps, smooth curve
  - Area fill: linear gradient, emerald 35% opacity → 0% opacity, top to bottom
  - Gridlines: 5 faint horizontal lines, `#1D1D1D`, 1px
  - Hover state: one point highlighted with a ring marker + dashed vertical guide line, paired with a floating tooltip card (dark `#1A1A1A` bg, border, drop shadow) showing value + date
- **X-axis labels:** month abbreviations, 10px, `text-quaternary`, evenly spaced below chart

---

## 🧩 Component 5 — Performance Summary Panel

Right column of the main row (~36% width), stacked into 3 sub-blocks with 16px spacing between:

1. **Pair Performance** — up to 3 rows: pair name (12px, fixed width) + horizontal progress bar (5px height, `emerald` fill, dark track) + win-rate percentage (11.5px Bold, right-aligned)
2. **Session Performance** — same row pattern for London / New York / Asian sessions
3. **Weekday Performance** — small 5-column bar chart (Mon–Fri), bar height maps to relative performance, emerald for positive days, muted red for a losing day, single-letter day labels below

Each sub-block has a 10.5px uppercase eyebrow label (`text-quaternary`) above it.

---

## 🧩 Component 6 — Recent Trades Panel

Widest panel in the bottom row (~48% width).

- **Header:** "Recent Trades" title + "View All" link (emerald, right-aligned)
- **Table columns:** Pair · Direction · Result · R:R · P/L
  - Column headers: 10px uppercase, `text-quaternary`, bottom border
  - Pair cell: small emerald dot + bold white pair name
  - Direction: pill — Long = emerald-soft fill/text, Short = neutral dark fill with border
  - Result: colored text only (no pill) — Win = emerald, Loss = red-muted, Break-even = tertiary gray
  - P/L: bold, colored to match result polarity
- Row divider: 1px `border-soft`, no border on the last row

---

## 🧩 Component 7 — Trading Activity Panel

Middle-right panel in the bottom row (~30% width).

- **Heatmap grid:** 7 columns × 5 rows of 30×30px cells, `radius-sm` corners (3px), 6px gap
  - Profitable day → `emerald` fill (full or 50% opacity variant for lighter days)
  - Losing day → `red-muted` fill, 75% opacity
  - Break-even day → flat `#3A3A3A`
  - No-trade day → empty `panel` fill with `border-soft` outline only
- **Legend:** below the grid, 4 items in a row, 8×8px swatch + 10px label each — Profitable / Losing / Break-even / No trade

---

## 🧩 Component 8 — Quick Actions Panel

Top of the right-hand side stack (~22% width), stacked below into Trader Status.

Three stacked buttons, 8px gap, full width:
- **Add Trade** — primary style: `emerald-soft` fill + border, plus icon, white text
- **Import CSV** — secondary style: `panel-alt` fill, neutral border, download icon
- **Export** — secondary style, same as above, export icon

All buttons: 9px/11px padding, `radius-sm`, 14px icon + 12px Medium label, icon stroke always `emerald-text`.

---

## 🧩 Component 9 — Trader Status Panel

Bottom of the right-hand side stack, fills remaining vertical space.

Four stat rows, each with a bottom divider (`border-soft`) except the last:
| Label | Value treatment |
|---|---|
| Risk Today | Small horizontal progress bar (84px track, emerald fill) + bold percentage (1.2%) |
| Current Streak | Bold value in `emerald-text` — "4 Wins" |
| Rules Broken | Bold white value — "0 this week" |
| Discipline | Status pill — `emerald-soft` bg, dot + label, e.g. "Focused" |

Row layout: label left (`text-tertiary`, 11.5px), value/control right-aligned.

---

## 📐 Auto Layout Hierarchy

```
02 Dashboard
│
├── Grid Background (full-bleed, behind everything)
├── App (flex row)
│   ├── Sidebar (240px fixed)
│   │   ├── Brand (logo + wordmark + tagline)
│   │   ├── Nav (8 items, Dashboard active)
│   │   ├── Spacer
│   │   ├── Account Card
│   │   └── Version Label
│   │
│   └── Content (flex, fills remaining width)
│       ├── Top Bar (title · search · notifications · avatar)
│       ├── KPI Row (4 cards)
│       ├── Main Row
│       │   ├── Equity Curve Panel (large)
│       │   └── Performance Summary Panel
│       │       ├── Pair Performance
│       │       ├── Session Performance
│       │       └── Weekday Performance
│       └── Bottom Row
│           ├── Recent Trades Panel
│           ├── Trading Activity Panel
│           └── Side Stack
│               ├── Quick Actions Panel
│               └── Trader Status Panel
│
└── Bottom Accent Line (2px, full width, emerald 40%)
```

---

## Notes for Figma Recreation
- Build the 4 base panel/card styles (`panel`, `kpi-card`, `nav-item`, `pill/badge`) as **Figma components** first — nearly every section reuses them.
- Set up **color styles** and **text styles** from the token tables above before laying out frames — this mirrors the CSS variable system used in the HTML build and will keep both frames (Cover + Dashboard) visually locked together.
- The emerald progress bars (Pair/Session Performance, Risk Today) can all share one **auto-layout bar component** with a variable-width fill.
- Icons are simple 1.6–2px stroke line icons (24×24 viewbox) — Feather/Lucide-style. Any icon set in that family will match.
