# Multithreaded Programming Lab: Pthreads & OpenMP

A comprehensive laboratory experiment analyzing thread creation, execution scheduling, workload distribution, race conditions, synchronization mechanisms, and performance scalability using POSIX Threads (Pthreads) and OpenMP.

## Benchmark Results & Scaling Analysis
The performance benchmark measures execution time for computing $10^9$ floating-point loop iterations across $1, 2, 4, 6,$ and $16$ threads. All runs produce a validated sum of $499,999,999,500.00$.
### Performance Data

| Threads ($p$) | Sequential Baseline | Pthreads Time | OpenMP Time | Pthreads Speedup | OpenMP Speedup | Pthreads Efficiency | OpenMP Efficiency |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 1.353219 s | 1.348142 s | 1.409294 s | 1.004× | 0.960× | 100.38% | 96.02% |
| **2** | — | 0.680737 s | 0.715560 s | 1.988× | 1.891× | 99.39% | 94.56% |
| **4** | — | 0.358872 s | 0.360803 s | 3.771× | 3.751× | 94.27% | 93.76% |
| **6** | — | 0.241345 s | 0.241608 s | 5.608× | 5.601× | 93.45% | 93.35% |
| **16** | — | 0.144812 s | 0.140692 s | 9.345× | 9.618× | 58.40% | 60.11% |

## Key Observations

Near-Linear Speedup: Both APIs scale well up to 6 threads, maintaining over 93% parallel efficiency.   
Diminishing Returns at 16 Threads: Efficiency decreases to ~58–60% at 16 threads due to hardware core limits, thread management overhead, lock contention, and memory bandwidth bottlenecks.  

## Build and Run
GuideEnvironment Prerequisites
Environment: Linux or WSL (Windows Subsystem for Linux). 
Compiler: GCC with OpenMP and Pthreads support (sudo apt install build-essential)

## Part A: POSIX Threads (Pthreads)
cd Pthreads

## Compile and run thread creation examples
gcc thread1.c -o thread1 -pthread && ./thread1
gcc thread2.c -o thread2 -pthread && ./thread2

## Array workload partitioning
gcc thread_sum.c -o thread_sum -pthread && ./thread_sum

## Race condition and Mutex resolution
gcc race.c -o race -pthread && ./race
gcc mutex.c -o mutex -pthread && ./mutex

## Performance testing
gcc pthread_perf.c -o pthread_perf -pthread && ./pthread_perf

## Part B: OpenMP Directives
cd Openmp

## Compile and run OpenMP region basics
gcc omp1.c -o omp1 -fopenmp && ./omp1

## Work sharing with reduction
gcc omp_sum.c -o omp_sum -fopenmp && ./omp_sum

## OpenMP race condition and critical section fix
gcc omp_race.c -o omp_race -fopenmp && ./omp_race
gcc omp_critical.c -o omp_critical -fopenmp && ./omp_critical

## Thread coordination via barrier
gcc omp_barrier.c -o omp_barrier -fopenmp && ./omp_barrier

## Performance testing
gcc omp_perf.c -o omp_perf -fopenmp && ./omp_perf

## Part C: Sequential Baseline
cd "Sequential baseline Performance analysis"
gcc sequential.c -o sequential && ./sequential

## Parallel Concepts Comparison

### Parallel Concepts Comparison

| Concept | POSIX Threads (Pthreads) | OpenMP |
| :--- | :--- | :--- |
| **API Paradigm** | Low-level C library calls[cite: 2] | High-level pragma directives[cite: 2] |
| **Thread Management** | Explicit (`pthread_create`, `pthread_join`)[cite: 2] | Implicit team management (`#pragma omp parallel`)[cite: 2] |
| **Loop Scheduling** | Manual calculation of index bounds per thread[cite: 2] | Automated loop distribution (`#pragma omp parallel for`)[cite: 2] |
| **Critical Section** | Manual Mutex locking (`pthread_mutex_lock`)[cite: 2] | Directive-based restriction (`#pragma omp critical`)[cite: 2] |
| **Reductions** | Manual partial sum aggregation[cite: 2] | Direct reduction syntax (`reduction(+:var)`)[cite: 2] |

## Directory Structure

```text
.
├── pthreads/
│   ├── thread1.c          # Single thread creation and joining demo
│   ├── thread2.c          # Multi-thread creation and OS scheduling test
│   ├── thread_sum.c       # Manual array workload distribution
│   ├── race.c            # Data race condition demonstration
│   ├── mutex.c           # Race condition resolution using mutex locks
│   └── pthread_perf.c    # Large workload performance benchmark
├── openmp/
│   ├── omp1.c            # Parallel region setup and thread ID extraction
│   ├── omp_sum.c         # Work sharing with reduction(+:sum) clause
│   ├── omp_race.c        # OpenMP data race demonstration
│   ├── omp_critical.c    # Mutual exclusion using #pragma omp critical
│   ├── omp_barrier.c     # Stage coordination using #pragma omp barrier
│   └── omp_perf.c        # Directive-based performance benchmark
└── sequential.c          # Single-threaded execution baseline
