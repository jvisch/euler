using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem023.CSharp
{
    class Program
    {
        static IEnumerable<int> nextInt(int startFrom)
        {
            int i = startFrom;
            do
            {

                yield return i;
                i++;
            } while (true);
        }
        
        static void Main(string[] args)
        {
            int max = 28123;

            //Enumerable.Range(1, 10).ToList().ForEach( x => Console.WriteLine(x));

            Func<int, IEnumerable<int>> divisors = value => from i in Enumerable.Range(1, value-1)
                                                  where value % i == 0
                                                  select i;
            
            Func<int, bool> isAbundant = i => divisors(i).Sum() > i;

            foreach (var i in nextInt(1))
            {
                if (!isAbundant(i))
                {
                    Console.WriteLine(i);
                }
            }

        }
    }
}