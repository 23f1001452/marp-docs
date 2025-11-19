---
marp: true
title: Product Documentation
paginate: true
author: SANJ
theme: default
class: lead
---

<!-- This slide includes your email -->
# Product Documentation  
#### Author: SANJ  
📧 23f1001452@ds.study.iitm.ac.in

---

# Why This Matters
- Documentation should be:
  - Maintainable in Git
  - Easy to version
  - Convertible into PDF, PPT, or HTML
- Marp allows all of this

---

<!-- Slide with background image -->
<!-- Change the image URL to something valid in your repo -->
<!-- Example uses an internet-hosted image -->
<!-- If using local, place image in repo and refer like: url(./images/bg.jpg) -->

<!--
backgroundImage: url(https://picsum.photos/1600/900)
backgroundSize: cover
backgroundColor: rgba(0,0,0,0.4)
class: invert
-->

# Documentation Vision  
A clean, simple, reusable documentation system.

---

# Custom Styling Example

<style>
h1 {
  color: #0066ff;
}
p {
  font-size: 18px;
}
</style>

This slide demonstrates **custom CSS styling** inside Marp.

---

# Mathematical Examples

Algorithmic complexity example:

$$
T(n) = 2T(n/2) + n
$$

Applying the Master Theorem:

$$
T(n) = O(n \log n)
$$

---

# Custom Theme Definition

You can also define your own theme:

```css
/* theme.css */
section {
  font-family: Arial, sans-serif;
}
h1 {
  color: #0099ff;
}
