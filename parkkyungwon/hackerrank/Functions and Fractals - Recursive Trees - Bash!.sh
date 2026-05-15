function dfs {
    local depth=$1
    if [ $depth -eq 0 ]; then return; fi

    local margin_a=$2
    local margin_b=$2
    local pre_margin=${pad::17}
    local num=$((2 ** (depth - 1)))
    local size=$((2 ** (5 - depth)))
    local output

    for _ in $(seq 1 $size); do
        output=$pre_margin
        output+=${pad::$(((margin_b + 1) / 2))}
    
        margin_a_txt=${pad::margin_a}
        margin_b_txt=${pad::margin_b}
        for _ in $(seq 1 $num); do
            output+="1${margin_a_txt}1${margin_b_txt}"
        done

        margin_a=$((margin_a - 2))
        margin_b=$((margin_b + 2))
        output+=$pad
        echo "${output::100}"
    done

    output=$pre_margin
    output+=${pad::$((size * 2))}
    margin=${pad::margin_b}
    for _ in $(seq 1 $num); do
        output+="1${margin}"
    done
    output+=$pad

    for _ in $(seq 1 $size); do
        echo "${output::100}"
    done

    dfs $((depth - 1)) $margin_b
}

pad="$(printf '_%.0s' $(seq 1 100))"

read n
num_of_lines_of_pad=$((2 ** (6 - n) - 1))

for _ in $(seq 1 $num_of_lines_of_pad); do
    echo "$pad"
done

dfs $n $num_of_lines_of_pad
