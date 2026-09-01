# Пост в LinkedIn про AIDAO 2025

Ограничения по стилю соблюдены. Многострочных перечислений нет, двоеточий нет, тире нет, конструкций «не X, а Y» нет. Дефисы остались только внутри имён собственных, Lift-Splat-Shoot, ResNet-50, bird's-eye. Это дефисы, а не тире.

---

## Основной вариант

```
Last November I spent 32 hours at HSE in Moscow building a bird's-eye view perception
model, and I still think about how much of the score came down to getting the geometry
right.

AIDAO is the AI and Data Analysis Olympiad run by Yandex Education and the HSE Faculty
of Computer Science. 248 teams from 14 countries entered and 30 reached the onsite
final. The online qualifier was a completely different problem about error correction
in quantum key distribution, and our team came through it in fourth place.

The final task came from Yandex's self-driving group. Given four calibrated cameras on
a car, reconstruct the static occupancy map around it, a grid of 188 by 126 cells
covering 150 meters ahead and 100 meters across. Scoring was mean IoU over free and
occupied cells, with unknown cells masked out.

I implemented Lift-Splat-Shoot from scratch in PyTorch. A shared ResNet-50 backbone
with an FPN merge produces the features, a depth head predicts a categorical
distribution over 64 depth bins, and every feature is smeared along its ray in
proportion to that distribution before it lands in the grid. There is no depth
supervision anywhere in the pipeline. The network learns depth from the occupancy
target alone.

What actually moved the score was calibration. Our first version precomputed the
projection geometry once and reused it for every frame. The dataset varies calibration
from frame to frame, so I moved the whole computation inside the forward pass. The
second half of that problem was quieter. Images are resized before the backbone while
the intrinsics describe the original frame, and the four cameras do not share a
resolution, so the pixel grid has to be mapped back into original image coordinates
before any ray is cast.

We finished at 0.5606 IoU on the private test set. The winning team scored 0.564.

Code and a full writeup are in the repo.

https://github.com/iluuua/aidao-2025-bev-occupancy
```

---

## Что проверить перед публикацией

**Четвёртое место в отборе** взято из переписки команды, а не из официальной таблицы. Если не уверен в цифре, убери предложение целиком, пост от этого не пострадает.

**Слово «I implemented»** стоит там, где ты писал код сам. Если часть модели писал сокомандник, замени на «we implemented» либо назови свою зону явно.

**Итоговое место команды в финале** в посте не заявлено намеренно, потому что я его не знаю. Если оно призовое, поставь его сразу после числа 0.5606.

**Название команды** «хихи-квадрат» в пост не вошло, шутка про хи-квадрат по-английски не читается. Если хочется человеческой детали, лучше добавь строку про ночной суп на 32-часовом финале, это переводится без потерь.

---

## Совсем короткая версия

```
32 hours at HSE in Moscow for the final of AIDAO, the AI and Data Analysis Olympiad run by
Yandex Education and the HSE Faculty of Computer Science. 248 teams from 14 countries entered
and 30 reached the final.

Yandex's self-driving team set the task. From four calibrated cameras on a car, reconstruct the
occupancy map around it as a 188 by 126 grid, scored by mean IoU. I built Lift-Splat-Shoot from
scratch in PyTorch. Most of the gain came from recomputing the projection geometry inside the
forward pass for every frame, because calibration varies between frames and the four cameras do
not share a resolution.

We finished at 0.5606 IoU on the private test set. The winning team scored 0.564.

Code and a full writeup are in the repo.

https://github.com/iluuua/aidao-2025-bev-occupancy
```

---

## Средняя версия

```
Last November our team spent 32 hours at HSE in Moscow on the final of AIDAO, the AI and
Data Analysis Olympiad run by Yandex Education and the HSE Faculty of Computer Science.
248 teams from 14 countries entered and 30 reached the final.

The task came from Yandex's self-driving group. Given four calibrated cameras on a car,
reconstruct the static occupancy map around it as a grid of 188 by 126 cells, scored by
mean IoU. I implemented Lift-Splat-Shoot from scratch in PyTorch, with a shared
ResNet-50 backbone, a depth head over 64 bins and a differentiable splat into the grid.
The biggest gain came from recomputing the projection geometry inside the forward pass
for every frame, since the calibration varies between frames and the four cameras do
not share a resolution.

We finished at 0.5606 IoU on the private test set, with the winning team at 0.564. Code
and a full writeup are in the repo.

https://github.com/iluuua/aidao-2025-bev-occupancy
```
