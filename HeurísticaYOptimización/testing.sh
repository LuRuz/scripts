#!/usr/bin/env bash

#Script para ejecutar pruebas de la práctica

NUM_EXAMPLES="6"  # Numero de ejemplos por heuristica
HEURISTICS=(hone htwo hthree noh)  # Heuristicas utilizadas para las pruebas
TIME_THRESH="400"  # Tiempo maximo de espera para un test


# Ejecuta el programa con la heuristica correspondiente
execTest() {
    EXAMPLE_FILE="$(readlink -e ejemplos/$1)"

    pushd solucion/ &>/dev/null
    touch $1.{output,statistics}
    popd &>/dev/null

    python3 busqueda/resolution.py \
            "$EXAMPLE_FILE" "$2" "solucion/$1.output" "solucion/$1.statistics"
}


# Pruebas de heuristica
for ((h=0; h < "${#HEURISTICS[*]}"; h++))
do
    echo "-------- HEURISTICA $h --------"
    for ((i=0; i <= $NUM_EXAMPLES; i++))
    do
        echo ""
        echo "PRUEBA $i"
        execTest "problema$i.prob" "${HEURISTICS[$h]}" &
        pid="$!"
        KILLED=0

        start_time="$(date +%s)"
        while pgrep python &>/dev/null
        do
            sleep 0.1
            end_time="$(date +%s)"
            if [[ "$(( end_time - start_time ))" -gt "$TIME_THRESH" ]]; then
                kill "$(pgrep python)" &>/dev/null
                echo -n "Proceso $pid terminado por superar $TIME_THRESH s"
                echo ""
                KILLED=1
            fi
        done
        if [[ $KILLED -eq 0 ]]; then
            cat "solucion/problema$i.prob.statistics"
        fi
    done
    echo "-------------------------------"
    echo ""

done
