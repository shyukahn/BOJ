#include <stdio.h>
#include <stdlib.h>

struct node {
    int start;
    int end;
    long long int sum;
};

typedef struct node *node_t;

node_t *generateTree(long long int *num_array, int N, int p) {
    
    node_t *tree = (node_t *)malloc(2 * N * sizeof(node_t));
    
    // init tree
    for (int i=0; i<2*N; i++) {
        tree[i] = (node_t)malloc(sizeof(struct node));
    }
    
    // init leafs
    for (int i=0; i<N; i++) {
        node_t leaf = tree[N + i];
        leaf -> start = i;
        leaf -> end = i;
        leaf -> sum = num_array[i];
    }
    
    //init nodes
    for (int i=N-1; i>0; i--) {
        node_t node = tree[i];
        node_t left = tree[2*i];
        node_t right = tree[2*i+1];
        
        node -> start = left -> start;
        node -> end = right -> end;
        node -> sum = (left -> sum) + (right -> sum);
    }
    
    return tree;
}

void replaceValue(node_t *tree, int N, int index, long long int value) {
    
    node_t leaf = tree[N + index];
    long long int change = value - (leaf -> sum);
    
    for (int i=N+index; i>0; i /= 2) {
        node_t node = tree[i];
        node -> sum = (node -> sum) + change;
    }
}

long long int getSum(node_t *tree, int N, int start, int end) {
    
    if (N == 1) {
        return tree[1] -> sum;
    }
    
    if (start == end) {
        return tree[N + start] -> sum;
    }
    
    int root_index = 1;

    node_t start_root = tree[2 * root_index];
    node_t end_root = tree[2 * root_index + 1];
    
    while (end < end_root -> start || start > start_root -> end) {
        if (end < end_root -> start) {
            root_index = 2 * root_index;
        } else {
            root_index = root_index * 2 + 1;
        }
        start_root = tree[2 * root_index];
        end_root = tree[2 * root_index + 1];
    }
    int start_index = root_index * 2;
    int end_index = root_index * 2 + 1;
    
    long long int sum = 0LL;
    
    while (start_root -> start != start) {
        node_t right = tree[start_index * 2 + 1];
        if (start < right -> start) {
            start_index = 2 * start_index;
            sum += right -> sum;
        } else {
            start_index = 2 * start_index + 1;
        }
        start_root = tree[start_index];
    }
    sum += start_root -> sum;
    
    while (end_root -> end != end) {
        node_t left = tree[end_index * 2];
        if (end > left -> end) {
            end_index = 2 * end_index + 1;
            sum += left -> sum;
        } else {
            end_index = 2 * end_index;
        }
        end_root = tree[end_index];
    }
    sum += end_root -> sum;
    
    return sum;
}

int main() {
    
    int N, M, K; 
    scanf("%d %d %d", &N, &M, &K);
    
    int newN = 1;
    int p = 0; // power of newN
    while (newN < N) {
        newN = newN << 1;
        p++;
    }
    
    long long int *num_array = (long long int *)malloc(newN * sizeof(long long int));
    
    // Generate num_array
    for (int i=0; i<N; i++) {
        long long int temp_num;
        scanf("%lld", &temp_num);
        num_array[i] = temp_num;
    }
    for (int i=N; i<newN; i++) { // fill 0s for remaining
        num_array[i] = 0LL;
    }
    
    node_t *tree = generateTree(num_array, newN, p);
    
    for (int i=0; i<M+K; i++) {
        int a, b;
        long long int c;
        scanf("%d %d %lld", &a, &b, &c);
        if (a == 1) {
            replaceValue(tree, newN, b - 1, c);
        } else {
            printf("%lld\n", getSum(tree, newN, b - 1, (int) c - 1));
        }
    }
    
    return 0;
}