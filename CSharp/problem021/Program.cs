using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem021.CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var xxxx = from i in Enumerable.Range(1, 10000)
                       select new { i = i,
                                    n = (from p in Enumerable.Range(1, i-1)
                                        where i % p == 0
                                        select p).Sum()
                       };

            var blub = xxxx.ToDictionary(elm => elm.i, elm => elm.n);

            long sum = 0;
            foreach (var i in blub)
            {
                if (blub.ContainsKey(i.Value) && (i.Key != i.Value))
                {
                    if (blub[i.Value] == i.Key)
                    {
                        sum += i.Key;
                    }
                }
            }

            Console.WriteLine(sum);
      
        }

        private static IEnumerable<int> divisors(int n)
        {
            return from i in Enumerable.Range(1, n-1)
                   where n % i == 0
                   select i;
        }
    }
}
