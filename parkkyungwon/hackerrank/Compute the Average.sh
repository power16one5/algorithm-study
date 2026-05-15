read n

total=0
for _ in $(seq 1 $n); do
    read a
    total=$((total + a))
done

printf "%.3f\n" $(bc -l <<< "$total / $n")
