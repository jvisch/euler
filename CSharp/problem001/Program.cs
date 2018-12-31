using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem001.CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var result =
                from i in Enumerable.Range(1, 1000)
                where i % 3 == 0 || i % 5 == 0
                select i;
            Console.WriteLine(result.Sum());
            Console.ReadLine();
        }
    }
}
