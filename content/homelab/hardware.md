+++
date = '2026-11-01T09:00:00-07:00'
draft = false
title = 'Current Hardware'
weight = 2
tags = ['homelab', 'hardware']
summary = 'The machines in the lab: what each one runs, what it cost, and where it came from.'
+++

## Cluster

{{< rack-elevation >}}

| Name            |Role              | OS              | Device                           | Processor        | RAM        | Storage              | Cost                 |
|-----------------|------------------|-----------------|----------------------------------|------------------|------------|----------------------|----------------------|
|minovsky         | 1 · Managed Switch | RouterOS        | **Mikrotik CRS310-8G+2S+IN**     | 98DX226S         | 256 MB     | 32 MB                | $200 · Amazon        |
|rx78             | 5 · Kubernetes node | Arch Linux, k3s | **HP EliteDesk 800 G2**          | Intel i5-6500T   | 16 GB      | 512 GB SSD           | $70 · eBay           |
|mkii             | 4 · Kubernetes node | Arch Linux, k3s | **HP EliteDesk 800 G2**          | Intel i5-6500T   | 16 GB      | 256 GB SSD           | $70 · eBay           |
|zeta             | 3 · Kubernetes node | Arch Linux, k3s | **HP EliteDesk 800 G2**          | Intel i5-6500T   | 16 GB      | 256 GB SSD           | $70 · eBay           |
|zz               | GPU Node         | Ubuntu 24.04    | **Custom Built** Details below   | AMD Ryzen 5 5500 | 32 GB      | 2 TB SSD             | $825 · Newegg, eBay  |

## GPU Node

{{< core-v1-elevation >}}

| Component   | Model                                 | Price |
| ------------|---------------------------------------|-------|
| Motherboard | MSI B450i motherboard                 | $130  |
| Graphics    | EVGA RTX 3060 12GB                    | $250  |
| Processor   | AMD Ryzen 5 5500                      | $90   |
| RAM         | Corsair Vengeance DDR4 2400MHz 32GB   | $90   |
| Storage     | 2 TB SSD (eBay)                       | $140  |
| Power       | EVGA 650W B5 PSU                      | $75   |
| Case        | Thermaltake Core V1                   | $50   |
| OS          | Ubuntu Server 24.04                   | $0    |
| Total       |                                       | $825  |

## Daily Driver

{{< t480-elevation >}}

| Name            |Role              | OS              | Device                           | Processor        | RAM        | Storage              | Cost                 |
|-----------------|------------------|-----------------|----------------------------------|------------------|------------|----------------------|----------------------|
|newtype-1        | Daily Driver     | Fedora Workstation | **Lenovo ThinkPad T480**         | Intel i5-8350U   | 32 GB      | 512 GB NVMe SSD      | $300 · eBay          |

## Inactive

| Name            |Role              | OS              | Device                           | Processor        | RAM        | Storage              | Cost                 |
|-----------------|------------------|-----------------|----------------------------------|------------------|------------|----------------------|----------------------|
|anaheim          | Spare            | TrueNAS Scale   | **HP Z2 Gen 4 SFF**              | Intel i7-8700T   | 32 GB      | 1 TB SSD, 2 TB HDD   | $140 · Facebook      |
|zakuii           | Spare            | Arch            | **Lenovo ThinkPad X250**         | Intel i5-5300U   | 8 GB       | 256 GB SSD           | $150 · Craigslist    |
