---
layout: lesson
title: "Python में नाम और मान"
summary: चर के नाम रखें, मान का प्रकार पहचानें, और मान को सही ढंग से बदलें।
permalink: /learning/translations/hi/python-variables/
id: hi-python-variables-001
content_type: lesson
category: programming-languages
language: hi
content_origin: translation
translation_of: python-variables-001
translation_status: draft
direction: ltr
difficulty: beginner
tags: [python, variables, data-types, हिंदी]
prerequisites: []
learning_objectives:
  - किसी मान को स्पष्ट नाम देना।
  - टेक्स्ट और संख्या के प्रकार में अंतर समझना।
  - एक सामान्य उदाहरण और सीमा वाले उदाहरण से व्यवहार जाँचना।
estimated_minutes: 20
content_status: drafted
review_status: pending
searchable: true
---

## सीखने के लक्ष्य

इस पाठ के बाद आप किसी मान को नाम दे सकेंगे, सामान्य प्रकारों में अंतर समझ सकेंगे, और असाइनमेंट तथा तुलना को अलग पहचान सकेंगे। यह पृष्ठ अंग्रेज़ी वाले [मूल पाठ]({{ '/learning/lessons/python-variables/' | relative_url }}) का स्वतंत्र हिंदी अनुवाद है। इसे अभी भाषा-संपादक से समीक्षा नहीं मिली है।

## पहले से क्या जानना चाहिए

प्रोग्रामिंग का पूर्व अनुभव आवश्यक नहीं है। Python चलाने का तरीका और टेक्स्ट एडिटर चाहिए। कोड के शब्द अंग्रेज़ी में ही रखे गए हैं क्योंकि Python के कीवर्ड और नाम उसी रूप में लिखे जाते हैं।

## मान को नाम देना

चर ऐसा नाम है जो प्रोग्राम चलते समय किसी मान को दर्शाता है। `=` दाईं ओर के मान को पहले निकालता है और फिर उसका परिणाम बाईं ओर के नाम को देता है।

```python
student = "Amina"
completed_lessons = 3
minutes_per_lesson = 20
study_minutes = completed_lessons * minutes_per_lesson
print(student, "ने", study_minutes, "मिनट पढ़ाई की")
```

अपेक्षित आउटपुट: `Amina ने 60 मिनट पढ़ाई की`। नाम से उसका उपयोग समझ आना चाहिए; `study_minutes` ऐसा स्पष्ट नाम है।

## प्रकार पहचानें

टेक्स्ट का प्रकार `str`, पूर्ण संख्या का `int`, और दशमलव संख्या का `float` होता है। टेक्स्ट `"4"` और संख्या `4` दिखने में मिलते-जुलते हैं, लेकिन गणना में अलग तरह से काम करते हैं।

```python
course = "Python basics"
lesson_count = 4
print(type(course).__name__)
print(type(lesson_count).__name__)
```

अपेक्षित आउटपुट की दो पंक्तियाँ `str` और `int` हैं।

## आम गलतियाँ

- `=` मान देता है; `==` दो मानों की समानता पूछता है।
- नाम में `-` लगाने पर Python उसे घटाव मानता है; `lesson_count` जैसा underscore वाला नाम लिखें।
- टेक्स्ट `"4"` और संख्या `2` को सीधे जोड़ने पर `TypeError` आता है। ज़रूरत हो तो `int("4")` से स्पष्ट रूपांतरण करें।
- जिस नाम को अभी मान नहीं दिया, उसे पढ़ने पर `NameError` आता है।

## अभ्यास

किताब के कुल पन्ने और पढ़े गए पन्ने अलग नामों में रखें। बाकी पन्ने छापें। शून्य पन्ने पढ़ने, कुछ पन्ने पढ़ने, और सभी पन्ने पढ़ने की स्थितियाँ जाँचें। हर बार कोड चलाने से पहले अपेक्षित परिणाम लिखें।

## आगे क्या पढ़ें

इसके बाद [Python में loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}) और [चार-सप्ताह का अध्ययन-पथ]({{ '/learning/courses/' | relative_url }}) देखें।
