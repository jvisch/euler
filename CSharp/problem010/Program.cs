using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem010
{
    class Program
    {
        static IEnumerable<int> Numbers(int start, int max)
        {
            while (start <= max )
            {
                yield return start;
                start++;
            }
        }

        static IEnumerable<long> Primes(int max)
        {
            List<int> primes = new List<int>() { 2 };
            foreach (var p in primes)
            {
                yield return p;
            }

            foreach (var n in Numbers(2, max))
            {
                bool isPrime = true;
                foreach (var p in primes)
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
            //long total = 0;
            //foreach (var x in Primes(2000000))
            //{
            //    Console.Write(x);
            //    total += x;
            //    Console.WriteLine(": " + total);
            //}

            Console.WriteLine(Primes(2000000).Sum());
            
            Console.ReadLine();
        }
    }
}
