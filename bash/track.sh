#!/bin/bash
track () {
    if [ $(grep -i -c "LOGFILE" ~/.bashrc) == 0 ]; then
            echo 'export LOGFILE="$HOME/.local/share/.timer_logfile"' >> ~/.bashrc
    fi

    if [ $( find ~/.local/share -name ".timer_logfile" | wc -l ) == 0 ]; then
            touch $LOGFILE
    fi

    if [ $1 == "start" ]; then 
        if [ "$( tail -n 1 $LOGFILE | cut -d" " -f1 )" == "LABEL" ]; then
            echo "A task is already running, use track stop to end current task before starting a new task"; return 0
        fi
        label=$2
        start_time=$(date +%T)
        echo "START $(date +%a) $(date +%b) $(date +%d) $start_time CEST $(date +%Y)" >> $LOGFILE
        echo "LABEL $label" >> $LOGFILE

    elif [ $1 == "stop" ]; then
        if [ "$( tail -n 1 $LOGFILE | cut -d" " -f1 )" != "LABEL" ]; then
            echo "No task running that can be stopped, you can start a task by using track start [label]"; return 0
        fi

        stop_time=$(date +%T)
        echo "END $(date +%a) $(date +%b) $(date +%d) $stop_time CEST $(date +%Y)" >> $LOGFILE
        echo "" >> $LOGFILE

    elif [ $1 == "status" ]; then
        if [ "$( tail -n 1 $LOGFILE | cut -d" " -f1 )" != "LABEL" ]; then
            echo "No task is running"; return 0
        fi
        echo "The currently running task is:"
        echo "$label"
    
    elif [ $1 == "log" ]; then
        lognumber=$( grep "START" $LOGFILE | cut -d" " -f5)
        
        declare -i counter
        counter=1
        for t in $lognumber; do
            start_clock=$( grep "START" $LOGFILE | cut -d" " -f3-5 | head -n "$counter" | tail -n 1 )
            start_clock=$(date -d "$start_clock" "+%s")
            stop_clock=$( grep "END" $LOGFILE | cut -d" " -f3-5 | head -n "$counter" | tail -n 1 )
            stop_clock=$(date -d "$stop_clock" "+%s")

            echo "$(((stop_clock-start_clock)/3600))"
            printf -v time_hour "%02d" $(((stop_clock-start_clock)/3600))
            printf -v time_min "%02d" $(((stop_clock-start_clock)/60-time_hour*60))
            printf -v time_sec "%02d" $(((stop_clock-start_clock)-time_min*60-time_hour*3600))
            
            echo "Task $counter: $time_hour:$time_min:$time_sec"
            counter=$(($counter+1))
        done
    else
        echo "Not a valid argument, the valid arguments are start [label], stop, status, log"
    fi
}
#ls -a ~/
#ls -a ~/.local/share