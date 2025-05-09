Hi Jason,

This is my solution to the problem set 12.

(a) `a1.png`: 20 by 20 grids, 10,000 iteratons, T = 10.\
Cluster size: around 10.\
    `a2.png`: 20 by 20 grids, 10,000 iteratons, T = 5.\
Cluster size: around 10 as well.\
    `a3.png`: 20 by 20 grids, 10,000 iteratons, T = 4.\
Cluster size: around 20.\
    `a4.png`: 20 by 20 grids, 10,000 iteratons, T = 3.\
Cluster size: around 30.\
    `a5.png`: 20 by 20 grids, 10,000 iteratons, T = 2.5.\
Cluster size: 40 or so.
- The cluster is growing with lower temperature.\

(c) `b1.png`: 40 by 40 grids, 10,000 iteratons, T = 10.\
    `b2.png`: 40 by 40 grids, 10,000 iteratons, T = 5.\
    `b3.png`: 40 by 40 grids, 10,000 iteratons, T = 4.\
    `b4.png`: 40 by 40 grids, 10,000 iteratons, T = 3.\
    `b5.png`: 40 by 40 grids, 10,000 iteratons, T = 2.5.
- The cluster size is bigger now, because we have larger lattice and thus more grids to put the clusters.

(b) `c1.png`: 20 by 20 grids, 10,000 iteratons, T = 2.\
    Mean Magnetization: 46\
    `c2.png`: 20 by 20 grids, 10,000 iteratons, T = 1.5.\
    Mean Magnetization: 280\
    `c3.png`: 20 by 20 grids, 10,000 iteratons, T = 1.\
    Mean Magnetization: -174

(d) `d.png`: 10 by 10 grids, 100,000 iteratons, T = 2.5.
- This similar to what we had for T = 2.5, but because we have more iterations now, they form even larger domain, which is even more than half the grids.

(e) `e1.png`: 20 by 20 grids, 100,000 iteratons, T = 2.5.\
    `e2.png`: 50 by 50 grids, 200,000 iteratons, T = 2.4.\
    `e3.png`: 100 by 100 grids, 300,000 iteratons, T = 2.3.\
    `e4.png`: 200 by 200 grids, 1,000,000 iteratons, T = 2.27.
- Clearly, this does not happen in `e4.png`, but it does form very large domain, when temperature and lattice is growing larger. And with more iterations, more and more small domains start connecting with each other. Therefore, the cluster will go to infinity with large iterations and large lattice.

## Contributions
- Sherlock Zhao
- Last Modified 5/9/2025