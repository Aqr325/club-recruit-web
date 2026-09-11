---
version: alpha
name: 科创部新伙伴共创计划·蓝色科技版扫码网页
description: 为科技创新工作室/科创部招新海报设计的二维码落地页，延续海报的蓝色科技商务风格，传递「共创、成长、专业」的社团形象。
colors:
  primary: "#2563eb"
  primary-light: "#3b82f6"
  secondary: "#dbeafe"
  tertiary: "#0ea5e9"
  neutral: "#f0f6ff"
  surface: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#1e3a8a"
  on-tertiary: "#ffffff"
  muted: "#64748b"
  text: "#0f172a"
typography:
  display:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 38px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.01em
  headline:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
  body:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em
  stat:
    fontFamily: "DIN Alternate, DIN, PingFang SC, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1
rounded:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    typography: "{typography.label}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
    typography: "{typography.label}"
---

## Overview

科创部新伙伴共创计划落地页延续海报「蓝色科技商务风」的调性，目标是让新生扫码后快速建立对科创部的专业感与共创感，并产生加入意愿。整体采用深蓝主色 + 浅蓝辅助 + 白色卡片，营造「理性、可信、有成长空间」的学生科创组织氛围。结构延续多页面可跳转：首页 → 了解我们 → 四大部门 → 加入我们。

## Colors

- **Primary (#2563eb):** 科技蓝，用于主按钮、关键标题、强调图标，传递专业与信任。
- **Secondary (#dbeafe):** 浅蓝背景色，用于卡片、标签、辅助按钮，柔化整体视觉。
- **Tertiary (#0ea5e9):** 亮蓝，用于小装饰、hover 状态和次要强调。
- **Neutral (#f0f6ff):** 页面底色，营造清爽理性的氛围。
- **Surface (#ffffff):** 卡片、浮层面板背景。
- **Text (#0f172a):** 深蓝黑色文字，保证浅色背景下的可读性。
- **Muted (#64748b):** 辅助说明文字。

## Typography

中文系统字体栈，移动端零加载成本。标题使用粗体字重建立专业感；正文行距 1.7，提升阅读舒适度；数据使用 DIN Alternate 等工业感字体，与科技蓝调形成统一。

## Layout

移动端优先，单列流式布局，最大宽度 480px 居中。使用圆角卡片和浅蓝阴影构建层级。顶部 Hero 区域占据 70–100vh，底部固定 CTA 条持续引导报名。页面分段清晰：社团简介 → 组织架构 → 部门详情 → 加入我们。

## Elevation & Depth

通过浅蓝色柔和阴影（`0 8px 24px rgba(37,99,235,0.12)`）和卡片叠加营造深度，避免深色投影。重要按钮使用科技蓝 + 轻微悬浮阴影，制造「可点击」暗示。

## Shapes

- 按钮：全圆角胶囊形。
- 卡片：24px 大圆角。
- 图标：用线性几何风格 SVG/emoji 装饰，避免过度可爱。

## Components

### Button Primary
科技蓝背景，白色文字，全圆角，用于「立即报名」「加入我们」等核心转化。

### Button Secondary
浅蓝背景，深蓝文字，用于次要操作（查看部门、复制群号）。

### Card
白色圆角卡片，承载部门介绍、数据、报名信息。

### Badge
小胶囊标签，用于部门名称、荣誉标识、状态提示。

## Do's and Don'ts

- ✅ 使用蓝色系，与海报主视觉统一。
- ✅ 强调「共创、成长、赛事、项目」等专业关键词。
- ✅ 保持按钮在拇指可触区域，最小 48px。
- ✅ 报名入口在首屏和底部固定栏各出现一次。
- ❌ 不要使用粉色可爱元素，与当前海报割裂。
- ❌ 不要把组织架构文档全文照搬，要提炼要点。
- ❌ 避免使用需要登录或复杂授权的表单。
