function insertionSort!(arr::Array)
    for i in 2:length(arr)
        key = arr[i]
        j = i - 1

        while j >= 1 && arr[j] > key
            arr[j + 1] = arr[j]
            j -= 1
        end

        arr[j + 1] = key
    end
end

a = [6, 5, 3, 1, 8, 7, 2, 4]

println(a)

insertionSort!(a)

println(a)

