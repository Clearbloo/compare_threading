defmodule ElixirThreadsTest do
  use ExUnit.Case
  doctest ElixirThreads

  test "greets the world" do
    assert ElixirThreads.hello() == :world
  end
end
