{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c1973dd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "72 17\n",
      "44 23\n",
      "31 24\n",
      "1\n",
      "26\n",
      "6\n",
      "64 26\n",
      "85 22\n",
      "52 4\n",
      "99 18\n",
      "39 13\n",
      "54 9\n",
      "4\n",
      "23\n",
      "20\n",
      "20\n",
      "26\n",
      "72\n",
      "514\n"
     ]
    }
   ],
   "source": [
    "# Objet : [Price, Weigth]\n",
    "\n",
    "# [N objet]\n",
    "\n",
    "# Personne : Max weigth, [ Nmax objet]\n",
    "\n",
    "# [N personnes]\n",
    "\n",
    "def SuperSale(weigth, listObject):\n",
    "    if weigth < 0 :\n",
    "        return 0\n",
    "    if  len(listObject) == 0:\n",
    "        return 0\n",
    "    if weigth >= listObject[-1][\"weigth\"]:\n",
    "        return max(listObject[-1][\"price\"] + SuperSale(weigth - listObject[-1][\"weigth\"], listObject[:-1]), SuperSale(weigth, listObject[:-1]))\n",
    "    else :\n",
    "        return SuperSale(weigth, listObject[:-1])\n",
    "\n",
    "def groupPrice(group,listObject):\n",
    "    summ = 0\n",
    "    for i in range(len(group)) :\n",
    "        summ += SuperSale(group[i][\"weigth\"], listObject)\n",
    "\n",
    "    return summ\n",
    "\n",
    "\n",
    "nbTest = int(input())\n",
    "res = []\n",
    "for i in range(nbTest):\n",
    "    nbObject = int(input())\n",
    "    listObject = []\n",
    "    for i in range(nbObject):\n",
    "        price, weigth = input().split(\" \")\n",
    "        obj = {'price': int(price), \"weigth\" : int(weigth)}\n",
    "        listObject.append(obj)\n",
    "\n",
    "    groupSize = int(input())\n",
    "    group = []\n",
    "    for i in range(groupSize):\n",
    "        weigth = int(input())\n",
    "        obj = {'weigth': weigth}\n",
    "        group.append(obj)\n",
    "\n",
    "    res.append(groupPrice(group, listObject))\n",
    "\n",
    "for i in range(len(res)):\n",
    "    print(res[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "223932dc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
