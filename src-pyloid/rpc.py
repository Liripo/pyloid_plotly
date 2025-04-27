from pyloid.rpc import PyloidRPC, RPCContext

rpc = PyloidRPC()

@rpc.method()
async def plot() -> str:
    import plotly.graph_objects as go
    import numpy as np

    # 生成 10000 个随机点
    N = 10000
    x = np.random.rand(N) * 100
    y = np.random.rand(N) * 100

    # 创建 scattergl 图
    fig = go.Figure(
        data=go.Scattergl(
            x=x,
            y=y,
            mode='markers',
            marker=dict(
                color='rgba(17, 157, 255, 0.5)',
                size=4,
            )
        )
    )

    # 设置布局
    fig.update_layout(
        title='ScatterGL 10000 Points Example (Python)',
        height=600,
        width=800,
    )

    return fig.to_json()


@rpc.method()
async def create_window(ctx: RPCContext):
    win = ctx.pyloid.create_window(title="Google Window")
    win.load_url("https://www.google.com")
    win.show_and_focus()