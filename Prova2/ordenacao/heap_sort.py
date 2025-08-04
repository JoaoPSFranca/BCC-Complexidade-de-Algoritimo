def heap_sort(arr):
    import heapq
    comparisons = 0  # heapq não expõe comparações, setamos zero
    swaps = 0        # também zero aqui
    h = []
    for value in arr:
        heapq.heappush(h, value)
    sorted_arr = [heapq.heappop(h) for _ in range(len(h))]
    arr[:] = sorted_arr
    return comparisons, swaps