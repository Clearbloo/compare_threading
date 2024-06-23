use tokio::task;
use tokio::time;
use tokio::time::Duration;

async fn thread(num_tasks: i32) -> Vec<task::JoinHandle<()>> {
    let mut tasks = Vec::new();
    for n in 0..num_tasks {
        tasks.push(task::spawn(async move {
            match n % 3 {
                0 => {
                    time::sleep(Duration::from_millis(1000)).await;
                }
                _ => time::sleep(Duration::from_millis(100)).await,
            }
            // println!("Hello {}", n)
        }));
    }
    tasks
}

#[tokio::main]
async fn main() {
    let tasks = thread(100000).await;
    for t in tasks {
        t.await.unwrap();
    }
}
