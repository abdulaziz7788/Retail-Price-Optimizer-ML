# Team Presentation Q&A

This file is for team members to prepare for possible professor questions during
the final presentation. Each question includes a short English answer and an
Arabic translation.

## 1. What Is The Dataset?

**English:**
We used the Brazilian E-Commerce Public Dataset by Olist. It contains real
e-commerce order information such as order items, product details, freight
value, product category, and price. For model training, we used the prepared
feature-engineered file: `dataset/feature_engineered_dataset.csv`.

**Arabic:**
استخدمنا مجموعة بيانات التجارة الإلكترونية البرازيلية من Olist. تحتوي على
معلومات طلبات حقيقية مثل عناصر الطلب، تفاصيل المنتجات، قيمة الشحن، فئة المنتج،
والسعر. في تدريب النموذج استخدمنا الملف المجهز بعد هندسة الخصائص:
`dataset/feature_engineered_dataset.csv`.

## 2. Why Did You Choose This Dataset?

**English:**
We chose it because it is realistic, structured, and suitable for a supervised
machine learning regression problem. It includes product and freight attributes
that can help predict item price.

**Arabic:**
اخترنا هذه البيانات لأنها واقعية ومنظمة ومناسبة لمشكلة تعلم آلي بإشراف من نوع
الانحدار. كما تحتوي على خصائص للمنتجات والشحن تساعد في التنبؤ بسعر المنتج.

## 3. What Is The Project Goal?

**English:**
The goal is to build a Retail Price Optimizer that predicts product price in BRL
using product, freight, category, size, and demand-count features. The model can
support pricing decisions instead of relying only on fixed markup rules.

**Arabic:**
هدف المشروع هو بناء نظام Retail Price Optimizer يتنبأ بسعر المنتج بالريال
البرازيلي باستخدام خصائص المنتج والشحن والفئة والحجم ومؤشرات الطلب. النموذج
يساعد في دعم قرارات التسعير بدلا من الاعتماد فقط على نسبة ربح ثابتة.

## 4. What Is The Target Variable?

**English:**
The target variable is `price`, which represents the item price in BRL.

**Arabic:**
المتغير الهدف هو `price`، وهو يمثل سعر المنتج بالريال البرازيلي.

## 5. Is This Classification Or Regression?

**English:**
This is a regression problem because the model predicts a continuous numeric
value, which is the product price.

**Arabic:**
هذه مشكلة انحدار وليست تصنيف، لأن النموذج يتنبأ بقيمة رقمية مستمرة وهي سعر
المنتج.

## 6. What Does Optimization Mean In This Project?

**English:**
Optimization here means choosing the model and settings that minimize prediction
error. We optimized the machine learning model using validation MAE, not by
directly maximizing profit or demand.

**Arabic:**
المقصود بالتحسين هنا هو اختيار النموذج والإعدادات التي تقلل خطأ التنبؤ. قمنا
بتحسين نموذج التعلم الآلي بناء على MAE في التحقق، وليس تعظيم الربح أو الطلب
بشكل مباشر.

## 7. Why Did You Use Machine Learning Instead Of A Simple Formula?

**English:**
A simple formula may miss nonlinear relationships between price, freight,
product weight, product size, category, and demand. Machine learning can learn
these interactions from historical data.

**Arabic:**
المعادلة البسيطة قد لا تلتقط العلاقات غير الخطية بين السعر والشحن ووزن المنتج
وحجمه وفئته والطلب عليه. التعلم الآلي يستطيع تعلم هذه العلاقات من البيانات
التاريخية.

## 8. Which Models Did You Test?

**English:**
We tested Linear Regression as a baseline, Random Forest Regressor, and Gradient
Boosting Regressor.

**Arabic:**
اختبرنا Linear Regression كنموذج أساسي للمقارنة، و Random Forest Regressor، و
Gradient Boosting Regressor.

## 9. Why Did You Use Linear Regression As A Baseline?

**English:**
Linear Regression is simple and interpretable. It gives us a baseline so we can
measure whether the more advanced models actually improve performance.

**Arabic:**
استخدمنا Linear Regression لأنه بسيط وسهل التفسير. يعطينا خط أساس نقارن به هل
النماذج المتقدمة حققت تحسنا فعليا أم لا.

## 10. Why Did Random Forest Perform Best?

**English:**
Random Forest handles nonlinear relationships and feature interactions well. It
also works strongly with structured tabular data, which matches our dataset.

**Arabic:**
أداء Random Forest كان الأفضل لأنه يتعامل جيدا مع العلاقات غير الخطية وتفاعل
الخصائص. كما أنه مناسب جدا للبيانات الجدولية المنظمة مثل بيانات مشروعنا.

## 11. Why Not Only Use Gradient Boosting?

**English:**
Gradient Boosting was tested, but in our run it had higher error than Random
Forest. We selected the model based on measured MAE, RMSE, and R2, not preference.

**Arabic:**
اختبرنا Gradient Boosting، لكن نتائجه في تجربتنا كانت أقل من Random Forest من
حيث الخطأ. اخترنا النموذج بناء على نتائج MAE و RMSE و R2 وليس بناء على تفضيل
مسبق.

## 12. What Hyperparameters Did You Test?

**English:**
For Random Forest, we tested `n_estimators` 80 and 140, `max_depth` 14 and None,
and `min_samples_leaf` 1. For Gradient Boosting, we tested `n_estimators` 80 and
140, `learning_rate` 0.05 and 0.10, and `max_depth` 2.

**Arabic:**
في Random Forest اختبرنا `n_estimators` بالقيم 80 و 140، و `max_depth` بالقيم
14 و None، و `min_samples_leaf` بالقيمة 1. في Gradient Boosting اختبرنا
`n_estimators` بالقيم 80 و 140، و `learning_rate` بالقيم 0.05 و 0.10، و
`max_depth` بالقيمة 2.

## 13. What Was The Best Result?

**English:**
The best model was Random Forest Regressor. On the holdout test set, it achieved
MAE 22.54 BRL, RMSE 53.09 BRL, and R2 0.775.

**Arabic:**
أفضل نموذج كان Random Forest Regressor. على مجموعة الاختبار حقق MAE بقيمة
22.54 BRL، و RMSE بقيمة 53.09 BRL، و R2 بقيمة 0.775.

## 14. What Does MAE Mean?

**English:**
MAE means Mean Absolute Error. In our project, MAE 22.54 means the model is off
by about 22.54 BRL on average.

**Arabic:**
MAE تعني متوسط الخطأ المطلق. في مشروعنا، MAE بقيمة 22.54 يعني أن النموذج يخطئ
في المتوسط بحوالي 22.54 ريال برازيلي.

## 15. What Does RMSE Mean?

**English:**
RMSE is Root Mean Squared Error. It gives a larger penalty to big mistakes, so it
helps us see whether the model makes large errors on unusual or expensive items.

**Arabic:**
RMSE تعني الجذر التربيعي لمتوسط مربعات الخطأ. تعطي عقوبة أكبر للأخطاء الكبيرة،
لذلك تساعدنا في معرفة هل النموذج يخطئ كثيرا في المنتجات غير المعتادة أو
الغالية.

## 16. What Does R2 Mean?

**English:**
R2 measures how much of the price variation is explained by the model. Our R2 of
0.775 means the model explains about 77.5% of the variation in the test data.

**Arabic:**
R2 تقيس مقدار التغير في السعر الذي يستطيع النموذج تفسيره. قيمة 0.775 تعني أن
النموذج يفسر تقريبا 77.5% من التغير في بيانات الاختبار.

## 17. How Did You Avoid Data Leakage?

**English:**
We removed columns that directly depend on the target price, such as
`total_order_item_value`, `freight_ratio`, `price_range`, `category_avg_price`,
`category_median_price`, and `price_vs_category_median`.

**Arabic:**
تجنبنا تسرب البيانات بحذف الأعمدة التي تعتمد مباشرة على السعر، مثل
`total_order_item_value` و `freight_ratio` و `price_range` و
`category_avg_price` و `category_median_price` و `price_vs_category_median`.

## 18. What Features Were Important?

**English:**
The most important features included `freight_value`, `product_weight_g`,
product description length, product demand count, product volume, and product
dimensions.

**Arabic:**
أهم الخصائص كانت `freight_value` و `product_weight_g` وطول وصف المنتج وعدد
الطلبات على المنتج وحجم المنتج وأبعاده.

## 19. Why Is Freight Value Important?

**English:**
Freight value is important because logistics cost is strongly connected to the
final price. Heavier or larger products often have higher shipping cost and
higher expected price.

**Arabic:**
قيمة الشحن مهمة لأن تكلفة النقل مرتبطة بشكل قوي بالسعر النهائي. المنتجات
الثقيلة أو الكبيرة غالبا يكون شحنها أعلى وسعرها المتوقع أعلى.

## 20. Why Did You Use One-Hot Encoding?

**English:**
The dataset has categorical columns such as product category, freight level, and
product size level. One-hot encoding converts these categories into numeric
columns that the model can understand.

**Arabic:**
تحتوي البيانات على أعمدة فئوية مثل فئة المنتج ومستوى الشحن ومستوى حجم المنتج.
استخدمنا One-Hot Encoding لتحويل هذه الفئات إلى أعمدة رقمية يستطيع النموذج
فهمها.

## 21. How Did You Split The Data?

**English:**
We used a 70/30 train-test split. The model trained on 70% of the rows and was
tested on 30% unseen rows.

**Arabic:**
قسمنا البيانات بنسبة 70/30. تم تدريب النموذج على 70% من الصفوف، وتم اختباره
على 30% من الصفوف التي لم يرها أثناء التدريب.

## 22. Did You Use Cross-Validation?

**English:**
Yes. We used cross-validation during GridSearchCV and also included a 10-fold
validation check on a sample to compare ensemble model stability.

**Arabic:**
نعم. استخدمنا التحقق المتقاطع أثناء GridSearchCV، وأضفنا فحص تحقق من 10 طيات
على عينة لمقارنة استقرار نماذج Ensemble.

## 23. Is The Model Ready For Real Business Use?

**English:**
It is ready as a decision-support baseline, but not as a full production pricing
system. A real business system should add competitor prices, inventory,
promotions, seasonality, and profit margin constraints.

**Arabic:**
النموذج جاهز كأداة مساعدة لاتخاذ القرار، لكنه ليس نظام تسعير إنتاجي كامل. في
الاستخدام الحقيقي نحتاج إضافة أسعار المنافسين والمخزون والعروض والموسمية
وقيود هامش الربح.

## 24. What Are The Main Limitations?

**English:**
The dataset does not include competitor prices, inventory levels, customer
demand elasticity, or live market conditions. Also, the model predicts expected
price, not guaranteed profit.

**Arabic:**
أهم القيود أن البيانات لا تحتوي على أسعار المنافسين أو مستوى المخزون أو مرونة
طلب العملاء أو ظروف السوق المباشرة. كذلك النموذج يتنبأ بالسعر المتوقع وليس
الربح المضمون.

## 25. How Can The Project Be Improved?

**English:**
We can improve it by adding competitor price data, product-level sales quantity,
seasonality, promotions, inventory, and a real optimization objective that
balances price, demand, and profit.

**Arabic:**
يمكن تحسين المشروع بإضافة بيانات أسعار المنافسين، كمية المبيعات لكل منتج،
الموسمية، العروض، المخزون، وهدف تحسين حقيقي يوازن بين السعر والطلب والربح.

## 26. What File Contains The Trained Model?

**English:**
The trained model is saved in `models/best_price_model.joblib`. It contains the
preprocessing pipeline and the trained Random Forest model.

**Arabic:**
النموذج المدرب محفوظ في `models/best_price_model.joblib`. يحتوي على خطوات
المعالجة المسبقة ونموذج Random Forest المدرب.

## 27. What Should Each Member Remember?

**English:**
Remember the dataset, the target variable, the model choices, why Random Forest
won, what MAE/RMSE/R2 mean, and why we removed leakage columns.

**Arabic:**
على كل عضو أن يتذكر مصدر البيانات، المتغير الهدف، النماذج المستخدمة، سبب تفوق
Random Forest، معنى MAE و RMSE و R2، وسبب حذف أعمدة تسرب البيانات.
