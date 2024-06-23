defmodule ElixirThreads do
  tasks =
    for n <- 0..100000 do
      Task.async(fn ->
        if rem(n, 3) == 0 do
          {:timer.sleep(1000)}
        else
          {:timer.sleep(100)}
        end
        # IO.puts("Hello #{n}")
      end)
    end

  Task.await_many(tasks, :infinity)
end
