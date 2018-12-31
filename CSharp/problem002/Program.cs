using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem002.CSharp
{
    class Program
    {
        static IEnumerable<int> GetNextFibo()
        {
            yield return 1;
            yield return 2;

            int a = 1;
            int b = 2;
            while (true)
            {
                int c = a + b;
                yield return c;
                a = b;
                b = c;
            }
        }

        

        static void Main(string[] args)
        {
            var result = (from fibo in GetNextFibo()
                         where fibo %2 == 0
                         select fibo).TakeWhile(f => f <= 4000000).Sum();
            Console.WriteLine(result );
            Console.Read();
        }
    }
}
