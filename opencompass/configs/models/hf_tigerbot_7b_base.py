from opencompass.models import HuggingFaceCausalLM

models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='tigerbot-7b-base',
        path='TigerResearch/tigerbot-7b-base',
        tokenizer_path='TigerResearch/tigerbot-7b-base',
        tokenizer_kwargs=dict(
            cache_dir=None,
            padding_side='left',
            truncation_side='left',
            padding=True,
            truncation=True
        ),
        max_out_len=100,
        max_seq_len=1024,
        batch_size=32,
        model_kwargs=dict(trust_remote_code=True, device_map='auto'),
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]
