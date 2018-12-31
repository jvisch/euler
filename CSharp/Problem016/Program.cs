using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ScottGarland;

namespace projectEuler.Problem016
{


    class Program
    {

        static void Main(string[] args)
        {
            // Check Add
            BigInteger bi = 2;
            for (int i = 1; i < 1000; i++)
            {
                bi *= 2;
            }
            Console.WriteLine(bi);

            var result = bi.ToString().ToCharArray().Select(c => int.Parse(c.ToString())).Sum();
            Console.WriteLine( result );

            Console.ReadLine();
        }


    }
}