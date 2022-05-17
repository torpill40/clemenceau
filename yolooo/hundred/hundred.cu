extern "C" __global__ void gen_binary_map(int *map, int m, int n)
{
    const int i = blockIdx.x * blockDim.x + threadIdx.x;
    const int j = blockIdx.y * blockDim.y + threadIdx.y;
    if (i < m && j < n)
    {
        map[i * n + j] = (i >> j) & 1;
    }
}
