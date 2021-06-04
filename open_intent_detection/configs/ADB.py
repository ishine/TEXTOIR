class ADB_Param():
    
    def __init__(self):
        
        self.hyper_param = self.get_hyper_parameters()

    def get_hyper_parameters(self):
        """
        Args:
            bert_model (directory): The path for the pre-trained bert model.
            num_train_epochs: The training epochs.
            max_seq_len (int): The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded.
            feat_dim (int): The feature dimension.
            warmup_proportion (float): The warmup ratio for learning rate.
            lr_boundary (float): The learning rate of the decision boundary.
            lr (float): The learning rate of backbone.
            loss_fct (str): The loss function for training.
            train_batch_size (int): The batch size for training.
            eval_batch_size (int): The batch size for evaluation. 
            wait_patient (int): Patient steps for Early Stop.
        """
        hyper_parameters = {

            'max_seq_length': None, 
            'freeze_bert_parameters': True,
            'feat_dim': 768,
            'warmup_proportion': 0.1,
            'lr_boundary': 0.05,
            'lr': 2e-5, 
            'loss_fct': 'cross_entropy',
            'train_batch_size': 128,
            'eval_batch_size': 64,
            'test_batch_size': 64,
            'wait_patient': 10

        }

        return hyper_parameters