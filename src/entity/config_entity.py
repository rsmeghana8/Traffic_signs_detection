from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_dir:Path
    train_images: Path
    test_images: Path
    train_labels: Path
    test_labels: Path
    val_images: Path
    val_labels: Path
    train_test_split: float
    train_val_split : float

@dataclass(frozen=True)
class TrainingConfig:
    params_epochs: int
    exp_name : str
    image_size: int
    freeze: int

@dataclass(frozen=True)
class EvaluationConfig:
    best_model: Path