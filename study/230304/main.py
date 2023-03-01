class PrimeFinder:
    def eratos(self,max_num):

        num_list = [True] * (max_num+1)
        num_list[0]=num_list[1]= False
        for i in range(2,max_num+1) :
            if num_list[i] :
                for j in range(i*2,max_num+1,i):
                    num_list[j] = False

        return num_list

    def loop(self,max_num):
        prime_list = [2]
        for i in range(3,max_num+1):
            for j in range(2,i):
                if not i%j :
                    break
            else :
                prime_list.append(i)
        return prime_list

    def improved_loop(self,max_num):
        prime_list = [2]
        for i in range(3, max_num + 1):
            for j in range(2, int(i**0.5)+1):
                if not i % j:
                    break
            else:
                prime_list.append(i)
        return prime_list