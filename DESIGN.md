---
version: alpha
name: 校级科创社团招新扫码网页
description: 为科技创新工作室招新海报设计的二维码落地页，延续海报的粉色、可爱、亲和风格，向新生传递社团定位、部门职责与报名入口。
colors:
  primary: "#c73a6a"
  secondary: "#ffd1dc"
  tertiary: "#ff9a3c"
  neutral: "#fff5f8"
  surface: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#3d2c33"
  on-tertiary: "#ffffff"
  muted: "#8a6e78"
  text: "#3d2c33"
typography:
  display:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 40px
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
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1
rounded:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 36px
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

科技创新工作室招新落地页延续海报「粉色、活泼、亲和」的调性，目标是让新生扫码后快速建立对社团的好感与信任，并产生报名意愿。整体采用高明度粉色系 + 圆润大圆角 + emoji/简笔插画式图标，营造「低门槛、高参与感」的学生组织氛围。三个版本分别对应三种招生策略：情感种草（粉萌版）、信息透明（架构版）、行动转化（报名表版）。

## Colors

- **Primary (#ff6b9d):** 主粉色，用于主按钮、强调标题、关键图标，传递活力与亲和力。
- **Secondary (#ffd1dc):** 浅粉色，用于背景、卡片、标签，柔和不刺眼。
- **Tertiary (#ff9a3c):** 暖橙色，用于次要强调、徽章、hover 状态。
- **Neutral (#fff5f8):** 页面底色，营造温暖轻盈的整体氛围。
- **Surface (#ffffff):** 卡片、浮层面板背景。
- **Text (#3d2c33):** 深褐粉色文字，保证浅色背景下的可读性。
- **Muted (#8a6e78):** 辅助说明文字。

## Typography

中文系统字体栈，确保移动端零加载成本。标题使用粗体字重建立青春感；正文行距 1.7，提升长文阅读舒适度；数据/数字使用 DIN Alternate 等工业感字体，与柔软的粉色调形成「理性+感性」的对比。

## Layout

移动端优先，单列流式布局，最大宽度 480px 居中。使用大量圆角卡片和柔和阴影构建层级。顶部 Hero 区域占据 70–100vh，底部固定 CTA 条持续引导报名。页面分段清晰，每段一个主题：社团简介 → 组织架构 → 部门详情 → 加入我们。

## Elevation & Depth

通过浅色柔和阴影（`0 8px 24px rgba(255,107,157,0.12)`）和卡片叠加营造深度，避免深色投影。重要按钮使用主粉色 + 轻微悬浮阴影，制造「可点击」的暗示。

## Shapes

- 按钮：全圆角胶囊形。
- 卡片：24px 大圆角。
- 头像/图标：圆形或超圆角。
- 装饰元素：使用 emoji 和简单几何图形（圆点、波浪、星星）替代复杂插画。

## Components

### Button Primary
主粉色背景，白色文字，全圆角，用于「立即报名」「加入我们」等核心转化。

### Button Secondary
浅粉背景，深褐粉文字，用于次要操作（查看部门、复制群号）。

### Card
白色圆角卡片，承载部门介绍、数据、报名信息。

### Badge
小胶囊标签，用于部门名称、荣誉标识、状态提示。

## Do's and Don'ts

- ✅ 使用 emoji 增加亲和力，但避免过度堆砌。
- ✅ 保持按钮在拇指可触区域，最小 48px。
- ✅ 报名入口在首屏和底部固定栏各出现一次。
- ❌ 不要使用深色科技风或商务冷色调，与海报割裂。
- ❌ 不要把组织架构文档全文照搬，要提炼要点。
- ❌ 避免使用需要登录或复杂授权的表单。
