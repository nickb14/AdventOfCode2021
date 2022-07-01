// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

string[] lines = File.ReadAllLines("/Users/nicholasbilsborrow/Code/nickb14/AdventOfCode2021/day11/input.txt");

int[,] grid = new int[lines.Length, lines[0].Length];

int i = 0;
foreach (string line in lines)
{
    int[] nums = Array.ConvertAll(line.ToCharArray(), c => (int)Char.GetNumericValue(c));
    
    int j = 0;
    foreach (int num in nums)
    {
        grid[i, j] = num;
        j++;
    }
    i++;
}