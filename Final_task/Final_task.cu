#include <cstdio>
#include <cstdlib>
#include <cuda_runtime.h>

float* loadCSV(const char* filename, int* numElements) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Failed to open file");
        return NULL;
    }

    int capacity = 1024;
    float* data = (float*)malloc(sizeof(float) * capacity);
    if (!data) {
        perror("malloc failed");
        fclose(file);
        return NULL;
    }

    int count = 0;
    while (fscanf(file, "%f,", &data[count]) == 1) {
        count++;
        if (count >= capacity) {
            capacity *= 2;
            float* temp = (float*)realloc(data, sizeof(float) * capacity);
            if (!temp) {
                perror("realloc failed");
                free(data);
                fclose(file);
                return NULL;
            }
            data = temp;
        }
    }

    fclose(file);
    *numElements = count;
    return data;
}

int main() {
    float* hostData;
    int numElements;

    hostData = loadCSV("Downloads/x_train.csv", &numElements);
    if (!hostData) return 1;

    // Print first 10 loaded values
    for (int i = 0; i < 10 && i < numElements; i++) {
        printf("Value %d: %f\n", i, hostData[i]);
    }

    float* deviceData;
    cudaError_t err;

    err = cudaMalloc((void**)&deviceData, numElements * sizeof(float));
    if (err != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed: %s\n", cudaGetErrorString(err));
        free(hostData);
        return 1;
    }

    err = cudaMemcpy(deviceData, hostData, numElements * sizeof(float), cudaMemcpyHostToDevice);
    if (err != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed: %s\n", cudaGetErrorString(err));
        cudaFree(deviceData);
        free(hostData);
        return 1;
    }

    // No kernel yet — just testing load and transfer

    cudaFree(deviceData);
    free(hostData);

    return 0;
}
