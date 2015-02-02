#!/bin/bash
#
#
#Test an algorithm with a set of parameters



usage() {
echo
echo "Usage: test [methode]"
echo "   Methodes:"
echo "      - brute_force"
echo "      - boyer_moore"
echo "      - rabin_karp"
echo "      - kmp"
echo
echo "exemple: test boyer-moore"

exit 1
}

if [ $# -lt 1 ]
then
    usage
fi

algo=""
#choix de l'algorithme
case $1 in
    brute_force | boyer_moore | rabin_karp | kmp)
	algo=$1;;
    *)
	echo -e "\nThis method doesn't exist"
	usage;;
esac

echo -e "\nMotif: \"AAAAA\""
/usr/bin/time -f "time: %E" python main.py -a $algo -m AAAAA

echo -e "\nMotif: \"GATACA\""
/usr/bin/time -f "time: %E" python main.py -a $algo -m GATACA


echo -e "\nMotif: \"GATACAGATACAGATACA\""
/usr/bin/time -f "time: %E" python main.py -a $algo -m GATACAGATACAGATACA  