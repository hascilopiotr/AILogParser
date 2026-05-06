import logging
import random
from datetime import datetime, timedelta
levels = ['INFO', 'WARN', 'ERROR']
modules = ['auth', 'db', 'api', 'parser', 'cache', 'payment', 'network']
messages = {
        'auth': {
            'INFO': [
                'User login successful',
                'User logout',
                'Password changed successfully',
                'Session created',
                'Token refreshed',
                'Two-factor authentication enabled',
            ],
            'WARN': [
                'Failed login attempt',
                'Token expiring soon',
                'Password complexity below recommended',
                'Suspicious login from new location',
                'Rate limit approaching for user',
            ],
            'ERROR': [
                'Invalid credentials',
                'Token expired',
                'Account locked after multiple failed attempts',
                'Session validation failed',
                'Authorization denied',
                'JWT signature verification failed',
            ],
        },
        'db': {
            'INFO': [
                'Database connection established',
                'Query executed successfully',
                'Transaction committed',
                'Backup completed',
                'Index rebuilt',
            ],
            'WARN': [
                'Slow query detected',
                'Connection pool near capacity',
                'Deadlock retry triggered',
                'Replication lag increasing',
                'Disk usage above 80%',
            ],
            'ERROR': [
                'Database connection timeout',
                'Query failed: syntax error',
                'Transaction rollback',
                'Connection pool exhausted',
                'Foreign key constraint violation',
                'Lost connection to primary node',
            ],
        },
        'api': {
            'INFO': [
                'Request received',
                'Response sent',
                'Endpoint registered',
                'API key validated',
                'Webhook delivered',
            ],
            'WARN': [
                'Request took longer than expected',
                'Deprecated endpoint called',
                'Rate limit warning',
                'Missing optional header',
                'Response payload near size limit',
            ],
            'ERROR': [
                'Internal server error',
                'Request validation failed',
                'Endpoint not found',
                'Unsupported media type',
                'Gateway timeout',
                'Webhook delivery failed',
            ],
        },
        'cache': {
            'INFO': [
                'Cache hit',
                'Cache populated',
                'Cache invalidated',
                'TTL refreshed',
            ],
            'WARN': [
                'Cache miss rate elevated',
                'Cache eviction triggered',
                'Memory usage high',
            ],
            'ERROR': [
                'Cache server unreachable',
                'Failed to write to cache',
                'Cache corruption detected',
            ],
        },
        'payment': {
            'INFO': [
                'Payment processed',
                'Refund issued',
                'Subscription renewed',
                'Invoice generated',
            ],
            'WARN': [
                'Payment retry scheduled',
                'Card expiring soon',
                'Currency conversion fallback used',
            ],
            'ERROR': [
                'Payment declined',
                'Payment gateway timeout',
                'Insufficient funds',
                'Invalid card number',
                'Fraud detection triggered',
                'Refund failed',
            ],
        },
        'parser': {
            'INFO': [
                'File parsed successfully',
                'Schema validated',
                'Records imported',
            ],
            'WARN': [
                'Malformed record skipped',
                'Encoding fallback used',
                'Unknown field encountered',
            ],
            'ERROR': [
                'File not found',
                'Invalid file format',
                'Schema validation failed',
                'Unexpected end of file',
            ],
        },
        'network': {
            'INFO': [
                'Connection established',
                'DNS resolved',
                'TLS handshake completed',
            ],
            'WARN': [
                'High latency detected',
                'Packet loss observed',
                'Retry attempt scheduled',
            ],
            'ERROR': [
                'Connection refused',
                'DNS resolution failed',
                'TLS handshake failed',
                'Network unreachable',
                'Connection reset by peer',
            ],
        },
    }

def generate_logs():

    with open('test_logs.log', 'w') as f:
        current_time = datetime(2025, 1, 1, 8, 0, 0, 0)
        for _ in range(1000):
            current_time += timedelta(seconds=random.randint(1, 15))

            timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')

            level = random.choices(levels, weights=[0.5, 0.2, 0.1])[0]
            module = random.choice(modules)
            message = random.choice(messages[module][level])
            log_entry = f"[{timestamp}] [{level}] [{module}] {message}\n"
            f.write(log_entry)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Generating synthetic log data...")
    generate_logs()
    logging.info("Log generation complete. Logs written to 'test_logs.log'.")
