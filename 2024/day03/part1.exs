defmodule Part1 do
  @spec solve(String.t()) :: String.t()
  def solve(data), do:
    Regex.scan(~r/mul\((?<first>\d+),(?<second>\d+)\)/, data)
    |> Enum.map(fn [_, first, second] -> [Integer.parse(first), Integer.parse(second)] end)
    |> Enum.map(fn [{first, _}, {second, _}] -> first*second end)
    |> Enum.sum()
end

File.read!("./2024/day03/input.txt") |> Part1.solve() |> IO.puts()
