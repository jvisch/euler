using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem004
{
    class Program
    {
        static IEnumerable<long> Getproduct()
        {
            for (int a = 999; a >99; a--)
                for (int b = 999; b > 99; b--)
                    yield return Math.BigMul(a,b);
        }

        static bool IsPalindrome(long value)
        {
            string s1 = value.ToString();
            if (s1.Length % 2 == 0)
            {
                for (int i = 0; i < s1.Length / 2; i++)
                {
                    if (s1[i] != s1[s1.Length - i - 1]) return false;
                }
                return true;
            }
            return false;
        }

        static void Main(string[] args)
        {
            var result = from v in Getproduct()
                         where IsPalindrome(v)
                         select v;
            //foreach (var v in result)
            //{
            //    Console.WriteLine( v );
            //}
            //Console.ReadLine();
            //Console.WriteLine();
            Console.WriteLine(result.Max());

            Console.ReadLine();
        }
    }
}
