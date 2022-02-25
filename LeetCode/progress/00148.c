
#include "problem.h"

int GetListLength(struct ListNode *head) {
    int list_length = 0;
    
    while (head) {
        list_length++;
        head = head->next;
    }
    return (list_length);
}

void CombineList(struct ListNode *head, int left, int pivot, int right) {
    int *sorted_val;
    int left_index = left;
    int right_index = pivot + 1;
    int sorted_index = 0;
    
    sorted_val = (int *)calloc(right - left + 1, sizeof(int));
    while (left_index <= pivot || right_index <= right) {
        if (left_index <= pivot && right_index > right) {
            // sorted_val[sorted_index] = 
            }
    }
}

void DivideListAndCombineList(struct ListNode *head, int left, int pivot, int right) {
    struct ListNode *sorted_list_node;
    
    if (left < right) {
        DivideList(head, 0, pivot / 2, pivot);
        DivideList(head, pivot + 1, (pivot + 1 + right) / 2, right)
    }
    CombineList(head, 0, pivot, right);
}

struct ListNode *sortList(struct ListNode *head) {
    int last_index_number;;
    
    last_index_number = GetListLength(head) - 1;
    DivideListAndCombineList(head, 0, last_index_number / 2, last_index_number);
    return (head);
}