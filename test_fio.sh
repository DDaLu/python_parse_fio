#!/bin/bash

FILENAME=/dev/sdb
RW=randwrite
RUNTIME=300
NUMJOBS=12
IODEPTH=32

echo "Test Disk Performance  filename="$FILENAME " read-write-mode="$RW " iodepth="$IODEPTH " numjobs="$NUMJOBS " runtime="$RUNTIME 
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=4k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_4k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=16k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_16k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=32k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_32k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=64k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_64k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=128k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_128k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=256k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_256k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=512k -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_512k
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=1M -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_1M
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=2M -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_2M
sleep(120)
fio -filename=$FILENAME -direct=1 -iodepth $IODEPTH -thread -rw=$RW -ioengine=libaio -bs=4M -runtime=$RUNTIME -numjobs=$NUMJOBS -group_reporting -name=test_4M