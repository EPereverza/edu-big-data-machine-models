# Глоссарий незнакомых вещей (обязательно)

Обновляйте этот файл **по ходу выполнения** ноутбуков, а не в конце.

Минимальные требования:
- добавить не менее 3 новых терминов на каждый ноутбук;
- для каждого термина указать простое объяснение своими словами;
- указать, где термин встретился в работе;
- добавить источник (URL, учебник, статья или ссылка на внутреннюю заметку).

| Термин | Простое объяснение своими словами | Где встретился в ЛР | Источник |
|---|---|---|---|
| `VarianceThreshold` | Удаляет признаки почти без разброса, которые обычно не помогают модели различать классы. | Notebook 1, шаг `Filter-методы`. | scikit-learn User Guide: Feature selection. |
| `mutual_info_classif` | Оценивает, насколько признак связан с таргетом, даже если связь нелинейная. | Notebook 1, сравнение filter-методов. | scikit-learn API: `mutual_info_classif`. |
| `f_classif` | ANOVA F-test: измеряет линейную разделимость классов по каждому признаку. | Notebook 1, filter-методы. | scikit-learn API: `f_classif`. |
| `abs_correlation` | Абсолютное значение корреляции признака с бинарным таргетом; простой линейный filter. | Notebook 1, filter-методы. | pandas/scipy: `corrcoef`. |
| `shortlist` | Компактный список лучших признаков по консенсусу нескольких методов (средний ранг). | Notebook 1, шаг 4. | README ЛР01, `build_shortlist`. |
| `Jaccard similarity` | Мера пересечения двух наборов: \|A∩B\| / \|A∪B\|; 1 = полное совпадение. | Notebook 1, задание 2; Notebook 2, method agreement. | Wikipedia / set similarity metrics. |
| `RFE` | Итерируется по признакам и постепенно убирает наименее полезные по мнению модели. | Notebook 2, wrapper-подходы. | scikit-learn API: `RFE`. |
| `SequentialFeatureSelector` | Жадный wrapper: добавляет (forward) признаки по одному, максимизируя CV-метрику. | Notebook 2, wrapper-методы. | scikit-learn API: `SequentialFeatureSelector`. |
| `L1 regularization` | L1-штраф обнуляет слабые коэффициенты → встроенный (embedded) отбор признаков. | Notebook 2, L1 LogisticRegression. | scikit-learn: L1 penalty. |
| `Permutation Importance` | Смотрит, насколько портится метрика, если случайно перемешать один признак. | Notebook 2 и 3, embedded/permutation анализ. | scikit-learn User Guide: permutation importance. |
| `stability_rate` | Доля прогонов, в которых признак был выбран; мера устойчивости отбора. | Notebook 2, задание 2. | ЛР01, `selection_stability.csv`. |
| `set_D_robust` | Feature set из признаков с высоким stability_rate (≥0.6) по нескольким random_state. | Notebook 2, задание 3. | ЛР01, самостоятельное задание. |
| `ROC-AUC` | Площадь под ROC-кривой; качество ранжирования положительного класса. | Notebook 3, сравнение моделей. | scikit-learn: `roc_auc_score`. |
| `class_weight` | Веса классов при обучении для балансировки несбалансированных данных. | Notebook 3, все модели. | scikit-learn: `class_weight`. |
| `threshold tuning` | Подбор порога отсечения score для компромисса precision/recall. | Notebook 3, задание 1. | `lab_utils.compute_threshold_metrics`. |
| `StratifiedKFold` | K-fold CV с сохранением доли классов в каждом fold. | Notebook 3, CV stability. | scikit-learn: `StratifiedKFold`. |
| `error_by_segment` | Анализ ошибок модели по сегментам (например, возрастные группы). | Notebook 3, задание 3. | `lab_utils.build_segment_error_table`. |
