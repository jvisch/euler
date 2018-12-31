using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem007
{
    class Program
    {
        static IEnumerable<int> Numbers(int start)
        {
            while (true)
            {
                yield return start;
                start++;
            }
        }

        static IEnumerable<int> Primes()
        {
            List<int> primes = new List<int>() { 2 };
            foreach (var p in primes)
            {
                yield return p;
            }
            foreach (var n in Numbers(primes.Max() + 1))
            {
                bool isPrime = true;
                foreach(var p in primes)
                {
                    if (n % p == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }

                if (isPrime)
                {
                    primes.Add(n);
                    yield return n;
                }
            }


        }


        static void Main(string[] args)
        {
            int i = 1;
            foreach (var p in Primes().Take(10001))
            {
                Console.WriteLine(i +": " + p);
                i++;
            }
            Console.ReadLine();
        }
    }
}
