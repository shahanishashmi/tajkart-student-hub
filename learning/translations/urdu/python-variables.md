---
layout: lesson
title: "Python میں نام اور values"
sitemap: false
robots: "noindex, follow"
summary: ڈیٹا کو نام دیں، اس کی قسم پہچانیں، اور value کو درست طریقے سے تبدیل کریں۔
permalink: /learning/translations/ur/python-variables/
id: ur-python-variables-001
content_type: lesson
category: programming-languages
language: ur
content_origin: translation
translation_of: python-variables-001
translation_status: draft
direction: rtl
difficulty: beginner
tags: [python, variables, data-types, اردو]
prerequisites: []
learning_objectives:
  - کسی value کو واضح نام دینا۔
  - متن اور عدد کی اقسام میں فرق کرنا۔
  - عام اور حدی مثالوں سے پروگرام کا رویہ جانچنا۔
estimated_minutes: 20
content_status: drafted
review_status: pending
searchable: true
---

## سیکھنے کے مقاصد

اس سبق کے بعد آپ کسی value کو نام دے سکیں گے، عام اقسام میں فرق کر سکیں گے، اور assignment کو comparison سے الگ پہچان سکیں گے۔ یہ انگریزی [اصل سبق]({{ '/learning/lessons/python-variables/' | relative_url }}) کا اردو ترجمہ ہے۔ ابھی کسی اردو زبان کے مدیر نے اس کا جائزہ نہیں لیا۔

## پہلے سے کیا جاننا چاہیے

پروگرامنگ کا سابقہ تجربہ ضروری نہیں۔ Python چلانے کا طریقہ اور ایک text editor درکار ہے۔ کوڈ کے الفاظ انگریزی میں ہیں کیونکہ Python کے keywords اور identifiers اسی شکل میں لکھے جاتے ہیں۔

## ایک value کو نام دیں

Variable ایسا نام ہے جو پروگرام چلتے وقت کسی value کی طرف اشارہ کرتا ہے۔ `=` پہلے دائیں طرف کی expression حل کرتا ہے، پھر نتیجہ بائیں طرف کے نام کو دیتا ہے۔

```python
student = "Amina"
completed_lessons = 3
minutes_per_lesson = 20
study_minutes = completed_lessons * minutes_per_lesson
print(student, "نے", study_minutes, "منٹ پڑھائی کی")
```

متوقع output: `Amina نے 60 منٹ پڑھائی کی`۔ ایسا نام چنیں جس سے معلوم ہو کہ value کس کام آتی ہے؛ `study_minutes` ایک واضح نام ہے۔

## value کی قسم دیکھیں

متن کی قسم `str`، مکمل عدد کی `int`، اور اعشاری عدد کی `float` ہے۔ متن `"4"` اور عدد `4` دکھنے میں ملتے ہیں لیکن حساب میں مختلف ہوتے ہیں۔

```python
course = "Python basics"
lesson_count = 4
print(type(course).__name__)
print(type(lesson_count).__name__)
```

متوقع دو outputs `str` اور `int` ہیں۔

## عام غلطیاں

- `=` value دیتا ہے؛ `==` دو values کا موازنہ کرتا ہے۔
- نام میں `-` لکھنے سے Python اسے تفریق سمجھتا ہے؛ `lesson_count` کی طرح underscore استعمال کریں۔
- متن `"4"` اور عدد `2` کو براہِ راست جمع کرنے سے `TypeError` آتا ہے۔ ضرورت ہو تو `int("4")` سے واضح تبدیلی کریں۔
- جس نام کو value نہ دی گئی ہو اسے پڑھنے سے `NameError` آتا ہے۔

## مشق

کتاب کے کل صفحات اور پڑھے گئے صفحات کو الگ نام دیں، پھر باقی صفحات دکھائیں۔ صفر صفحات، کچھ صفحات، اور تمام صفحات پڑھنے کی صورتیں آزمائیں۔ کوڈ چلانے سے پہلے متوقع جواب لکھیں۔

## اگلا قدم

اب [Python loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}) اور [چار ہفتوں کا مطالعہ منصوبہ]({{ '/learning/courses/' | relative_url }}) دیکھیں۔
