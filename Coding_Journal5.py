import math

def main():
    n = 1000 
    start = 0.0
    end = 2.0
    step = (end - start) / (n - 1)
    print("x\t sin(x)")
    for i in range(n):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t{y:.7f}")
if __name__ == "__main__":
    main()
