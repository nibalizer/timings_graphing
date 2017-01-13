Building Timings
================


This utility prints out timings of the first important buildings across
many games.


Important buildings:

* nexus
* hatch
* cc
* spawning pool
* spire
* gateway
* baracks


requirements
------------

Uses the ggtracker fork of sc2reader
Assumes a ``replays`` directory exists with many replays in it (searches recursively)


use
---

```shell
python timings.py
```


output
------


After running this on the IEM Shanghai and Gyeonggi sets you get:

```

CC timings [3949, 4531, 4530, 3995, 5914, 3817, 3864, 4576, 3907, 4173, 5749, 3881, 3872, 3864, 3881, 3842, 5654, 3835, 4480, 4647, 3939, 3910, 3907, 3947, 2917, 3880, 3836, 2955, 3940, 4497, 3892, 3877, 3848, 3790, 3844, 2964, 3897, 3803, 4011, 3805]
pool timings [2775, 2673, 2682, 2659, 2665, 1445, 2066, 2659, 3274, 2621, 2682, 2695, 2693, 2700, 2704, 2746, 3396, 2715, 2705, 2694, 2663, 2692, 2775, 2705, 2686, 2700, 2688, 1447, 2722, 2845, 2717, 2731, 2852, 2672, 2696, 2662, 2657, 2745, 3232, 2693, 2594, 2680, 2597, 2702, 2072, 2696, 2579, 2662, 1454, 2067, 2183, 2697, 2250, 2135, 2793, 2153, 2182, 2148, 1589, 2181, 1572, 2030, 2183, 2181, 1452, 2029, 2023, 2641, 1428, 2556, 2132, 2028, 2149, 2041, 2031, 2755, 1440, 1452, 23470, 3347, 2723]

```
