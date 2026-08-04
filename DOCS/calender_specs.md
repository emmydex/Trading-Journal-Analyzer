# 📅 FRAME 03 — CALENDAR

## Purpose
The Calendar answers "When am I trading well, and what happened on those days?" — connecting daily performance to journal reflection. Shares every token with Frame 02 (Dashboard) so the two frames feel like one continuous app.

---

## 📐 Frame Specifications

| Property | Value |
|---|---|
| Frame Name | 03 - Calendar |
| Frame Size | Desktop — 1440 × 1024 px |
| Layout | Two-column: fixed Sidebar (identical to Frame 02) + fluid Content |
| Background | `#0A0A0A` (Noir) |

---

## 🎨 Design Tokens
*Identical to Frame 02 — reuse the same Figma color/text styles.*

| Token | Hex / Value | Usage |
|---|---|---|
| `bg` | `#0A0A0A` | Frame background |
| `panel` | `#111111` | Default card/panel fill |
| `panel-alt` | `#141414` | Inputs, day cells (default/no-trade), account card |
| `border` | `#232323` | Standard 1px borders |
| `border-soft` | `#1B1B1B` | Subtle dividers, panel outlines |
| `emerald` | `#2E8B57` | Signature brand color — fills, selected state, win-rate bar |
| `emerald-text` | `#4CAE7C` | Emerald used as text/icon/today-ring |
| `emerald-soft` | `rgba(46,139,87,0.14)` | Active nav, selected day fill, badges, journal note bg |
| `emerald-soft-border` | `rgba(46,139,87,0.35)` | Borders on emerald-tinted elements |
| `red-muted` | `#9A5252` | Loss indicators only |
| `text-primary` | `#FFFFFF` | Headings, values |
| `text-secondary` | `#B3B3B3` | Body text, day numbers |
| `text-tertiary` | `#6E6E6E` | Captions, muted labels |
| `text-quaternary` | `#4A4A4A` | Eyebrows, axis labels, faintest text |

### Typography
Same pairing as Frame 01/02 — Space Grotesk for numerals/headings, Inter for body/labels.

### Spacing & Radius
Identical to Frame 02 — `radius-lg` 14px (panels), `radius-sm` 7px (day cells, buttons, nav items), 16px gutter between major panels, same content margins (26/24/32/32).

### Background
Same faint grid overlay as Frames 01–02 (36×36px, 2.8% white hairlines).

### Bottom Accent
Same as Frames 01–02: 2px full-width line, `#2E8B57` at 40% opacity, pinned to the frame's absolute bottom.

---

## 🧩 Component 1 — Sidebar
**Identical to Frame 02**, with one change: **Calendar** now carries the active state (emerald pill + left accent bar + emerald icon), Dashboard reverts to default styling. All other nav items, brand block, account card, and version label are unchanged — reuse the Frame 02 sidebar component and just swap which item is active.

---

## 🧩 Component 2 — Top Bar

Same anatomy as Frame 02 (title · search · notification · avatar), plus one addition:

| Element | Spec |
|---|---|
| Page title | "Calendar" — Space Grotesk SemiBold, 22px |
| Search field | 240px pill, same style as Dashboard |
| Notification icon | 34px circle, same as Dashboard |
| Avatar | 34px circle, same as Dashboard |
| **+ Add Trade button** | New — pill button, `emerald-soft` fill + `emerald-soft-border`, plus icon (14px, emerald stroke) + "Add Trade" label, 12.5px SemiBold white text, 8px/16px padding |

Layout: same space-between row, 12px gap between right-side controls.

---

## 🧩 Component 3 — Summary Bar

A single slim panel spanning the content width, **secondary in weight** to the calendar itself per spec.

- Panel: standard `panel` styling, but slimmer padding (14px vertical, no horizontal — padding lives on each stat instead)
- 5 stat groups in a row, each divided by a 1px `border-soft` vertical rule (no rule after the last item)
- Each stat: 10.5px uppercase eyebrow label (`text-quaternary`) + Space Grotesk Bold 20px value below
- **Net P&L** value only is colored `emerald-text` (or `red-muted` if negative) — the other four stay white

**Content:**
| Stat | Example |
|---|---|
| Trading Days | 18 |
| Winning Days | 11 |
| Losing Days | 5 |
| Break-even Days | 2 |
| Net P&L | +$1,779.05 (emerald) |

---

## 🧩 Component 4 — Calendar Panel

Left panel in the main row (~64% width — flex ratio 1.8 : 1 against the details panel).

### 4a. Calendar Header
- **Month nav (left):** prev-arrow circle button (28px, `panel-alt` fill) + month label ("July 2026", Space Grotesk Bold 18px, centered, 128px min-width) + next-arrow circle button
- **Right cluster:** small dot legend + "Today" pill button
  - Legend: 4 items, each a 7px dot + 10.5px label — Profit (emerald) / Loss (red-muted) / Break-even (`#3A3A3A`) / No trades (hollow, border only)
  - Today button: pill, `emerald-soft` fill/border, 11.5px SemiBold emerald text

### 4b. Weekday Header Row
7 equal columns, Mon → Sun, 10px uppercase `text-quaternary` labels, left-aligned with 9px inset to line up with day-number position below.

### 4c. Day Grid
5 rows × 7 columns, 6px gaps both directions, filling the remaining panel height. Each **day cell**:

| Property | Value |
|---|---|
| Corner radius | `radius-sm` (7px) |
| Default fill/border | `panel-alt` / `border-soft` |
| Padding | 8px / 9px |
| Internal layout | top row (day number + optional journal icon) → flexible spacer → P&L line → trade-count line |

**Day number:** Space Grotesk SemiBold 13px, `text-secondary` by default, promotes to white on profit/selected cells.
**Journal icon:** 12px notebook-outline icon, top-right of the cell, shown only on days with a saved entry; tinted `text-tertiary` normally, `emerald-text` on profit/selected cells.
**P&L line:** 12px Bold — emerald for profit, red-muted for loss, `text-tertiary` for break-even ($0.00). Omitted entirely on no-trade days.
**Trade count line:** 9.5px `text-quaternary`, e.g. "3 trades".

### Day Cell States (all defined as separate modifiers on the base cell)
| State | Treatment |
|---|---|
| **Default / No-trade** | `panel-alt` fill, `border-soft` border, no P&L or count shown |
| **Profitable** | Emerald wash fill (`rgba(46,139,87,0.10)`), emerald-tinted border (28% opacity), day number turns white |
| **Losing** | Red-muted wash fill (`rgba(154,82,82,0.09)`), red-muted-tinted border (26% opacity) |
| **Break-even** | Flat `#161616` fill, standard `border` outline, neutral gray $0.00 |
| **Outside current month** | Transparent fill, 38% opacity on the whole cell, muted day-number color |
| **Today** | 1.5px `emerald-text` ring border (layered on top of whatever P&L state the day has) + small 5px emerald dot next to the day number |
| **Selected** | `emerald-soft` fill + 1.5px solid `emerald` border, day number and journal icon promoted to white/emerald |
| **Hover** *(interactive only — not visible in static export)* | Recommend a subtle lightening of `panel-alt` or border brightening; define as a Figma interactive-component variant |
| **Disabled** | Same visual as "Outside current month" — reduced opacity, not clickable |

---

## 🧩 Component 5 — Day Details Panel

Right panel in the main row (~36% width), appears when a day is selected.

| Element | Spec |
|---|---|
| Date heading | "July 15, 2026" — Space Grotesk Bold 17px |
| Stat row (2-up) | **Trades** (22px Bold white) and **Daily P&L** (22px Bold, emerald if positive) side by side, each with a 10.5px uppercase label above |
| Win Rate | 10.5px label + 18px Bold value ("66.7%") + thin 6px progress bar below, emerald fill matching the percentage |
| **Best Trade card** | Row panel (`panel-alt`, `border-soft`, `radius-sm`): 9.5px uppercase tag "BEST TRADE" + 12.5px pair name on the left; bold 14px emerald value right-aligned |
| **Worst Trade card** | Same layout, red-muted value |
| Journal note | Full-width pill/banner, `emerald-soft` fill + border, notebook icon (15px, emerald) + 12px Medium white text — "Journal entry saved for this day" |
| Spacer | Flexible — pushes actions to the bottom of the panel |
| **View Trades** button | Primary style: `emerald-soft` fill/border, exchange-arrows icon (emerald), 12.5px SemiBold white, full width |
| **Open Journal** button | Secondary style: `panel-alt` fill, neutral border, notebook icon (`text-secondary`), full width |

---

## 📐 Auto Layout Hierarchy

```
03 Calendar
│
├── Grid Background (full-bleed, behind everything)
├── App (flex row)
│   ├── Sidebar (240px fixed — same component as Frame 02, Calendar active)
│   │
│   └── Content (flex, fills remaining width)
│       ├── Top Bar (title · search · notifications · avatar · + Add Trade)
│       ├── Summary Bar (5 secondary stats, divided row)
│       └── Main Row
│           ├── Calendar Panel
│           │   ├── Calendar Header (month nav · legend · Today button)
│           │   ├── Weekday Header Row (Mon–Sun)
│           │   └── Day Grid (5 rows × 7 day cells)
│           └── Day Details Panel
│               ├── Date Heading
│               ├── Stat Row (Trades · Daily P&L)
│               ├── Win Rate (value + bar)
│               ├── Best Trade Card
│               ├── Worst Trade Card
│               ├── Journal Note
│               ├── Spacer
│               └── Actions (View Trades · Open Journal)
│
└── Bottom Accent Line (2px, full width, emerald 40%)
```

---

## Notes for Figma Recreation
- Build the **day cell as a single component with variants** for every state in the table above (Default, Profitable, Losing, Break-even, Outside-month, Today, Selected, Hover, Disabled) — this is the piece you'll reuse most and the one most worth getting right as true variants rather than one-off frames.
- The **Today** and **Selected** states are visually independent (ring vs. fill) so they can combine — build them as two separate boolean properties on the day-cell component rather than one enum, in case a day is ever both.
- Reuse the Frame 02 **panel, pill/badge, and progress-bar components** as-is — the summary bar, legend badges, Today button, and win-rate bar all draw from the same components already built for the Dashboard.
- The **trade card** (Best/Worst Trade) is a new small component worth saving — it'll likely reappear in the Trades and Performance Analysis frames.
- Icons continue the same 1.6–2px stroke, 24×24 viewbox line-icon style used in Frames 01–02 (Feather/Lucide-style) — the notebook/journal icon here is the same glyph used for the Journal nav item in the sidebar.