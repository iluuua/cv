# Пост в LinkedIn про AIDAO 2025, версия с историей

Ограничения те же. Перечислений нет, двоеточий нет, тире нет, конструкций «не X, а Y» нет.

---

```
We slept about three hours that night.

Last November our team spent 32 hours at HSE in Moscow on the final of AIDAO, the AI and Data
Analysis Olympiad run by Yandex Education and the HSE Faculty of Computer Science. 248 teams from
14 countries entered and 30 reached the final. The task was set by Sergey Kim, who leads a
detection group in Yandex's autonomous transport team. From four calibrated cameras on a car,
reconstruct the occupancy map around it as a 188 by 126 grid, scored by mean IoU.

I built Lift-Splat-Shoot from scratch in PyTorch. Features come from a ResNet-50 shared across the
cameras, a depth head predicts a distribution over 64 depth bins, and every feature is smeared
along its ray in proportion to that distribution before it lands in the grid. There is no depth
supervision anywhere. The network learns depth from the occupancy target alone.

Then the night happened. We slept in shifts and I got about three hours.

I woke up, opened the laptop and changed two things before I was properly awake. I moved the
projection geometry inside the forward pass so that it is recomputed for every frame, because
calibration varies between frames and the four cameras do not share a resolution. Then I put a
squeeze and excitation block over the fused camera features, which is channel attention in
bird's-eye view.

I started training and went to get coffee. That run scored higher than everything else our team
submitted across the whole 32 hours.

We finished at 0.5606 IoU on the private test set. The winning team scored 0.564.

Code and a full writeup are in the repo.

https://github.com/iluuua/aidao-2025-bev-occupancy
```
