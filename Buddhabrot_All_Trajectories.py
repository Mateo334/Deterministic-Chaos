
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

n = 2000
m = 2000
max_val_real = (-2.0, 1.0)
max_val_imag = (-1.5, 1.5)

cnt = 10**6
iters = 10

zr = np.zeros(cnt, dtype=np.float32)
zi = np.zeros(cnt, dtype=np.float32)
cr = np.random.uniform(*max_val_real, cnt).astype(np.float32)
ci = np.random.uniform(*max_val_imag, cnt).astype(np.float32)

car = np.empty((iters, cnt, 2), dtype=np.float32)

escaped = np.zeros(cnt, dtype=bool)
active = np.ones(cnt, dtype=bool)
escape_step = np.full(cnt, iters, dtype=int)

for x in range(iters):
    t = zr[active].copy()
    zr[active] = t**2 - zi[active]**2 + cr[active]
    zi[active] = 2*t*zi[active] + ci[active]
    car[x, active, 0] = zr[active]
    car[x, active, 1] = zi[active]
    escaped_cur = active & (zr**2 + zi**2 > 4)
    active &= ~escaped_cur
    escaped |= escaped_cur
    escape_step[escaped_cur] = x + 1

valid = np.arange(iters)[:, None] < escape_step[None, :]
valid_escaped = valid & escaped[None, :]
valid_non_escaped = valid & (~escaped)[None, :]

points_escaped = car[valid_escaped]
points_non_escaped = car[valid_non_escaped]

def create_hist(points):
    hist, _, _ = np.histogram2d(points[:, 0],points[:, 1],bins=(n, m),range=[max_val_real, max_val_imag])
    return hist

box_escaped = create_hist(points_escaped)
box_non_escaped = create_hist(points_non_escaped)
box_all = box_escaped + box_non_escaped

fig, axes = plt.subplots(1, 3, figsize=(16, 9), dpi=240)
datasets = [
    (box_escaped, "Escaping trajectories"),
    (box_non_escaped, "Non-escaping trajectories"),
    (box_all, "All trajectories")
]

norm = PowerNorm(gamma=0.2, vmin=0, vmax=box_all.max())

for ax, (data, title) in zip(axes, datasets):
    im = ax.imshow(
        np.rot90(data.T, 1),
        cmap="turbo",
        norm=norm,
        extent=[*max_val_real, *max_val_imag],
        origin="lower",
        interpolation="nearest"
    )

    ax.set_title(title)
    ax.set_aspect("equal")

fig.colorbar(im, ax=axes, label="Number of visits", shrink=0.8)

# fig.savefig(
#     "buddhabrot.png",
#     dpi=240,
#     facecolor="white",
#     pad_inches=0.1
# )

plt.show()