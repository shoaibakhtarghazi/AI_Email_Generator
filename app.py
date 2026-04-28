import gradio as gr
from utils.email_generator import generate_email

with gr.Blocks() as app:

    gr.Markdown("# ✉️ AI Email Generator")

    points = gr.Textbox(lines=8, label="Bullet Points")

    tone = gr.Dropdown(
        ["professional", "friendly", "formal", "urgent"],
        value="professional",
        label="Tone"
    )

    recipient = gr.Textbox(value="client", label="Recipient Type")
    sender = gr.Textbox(value="Shoaib Akhtar Ghazi", label="Sender Name")
    subject = gr.Checkbox(value=True, label="Include Subject")

    btn = gr.Button("Generate Email")

    output = gr.Textbox(lines=15, label="Generated Email")

    btn.click(
        fn=generate_email,
        inputs=[points, tone, recipient, sender, subject],
        outputs=output
    )

app.launch(
    css="assets/style.css",
    share=True,
    debug=True
)