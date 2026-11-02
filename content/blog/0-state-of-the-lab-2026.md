+++
date = '2026-11-01T00:00:00-07:00'
draft = false
title = 'State of the Homelab, Late 2026'
image = '/images/state-of-the-lab.svg'
tags = ['homelab', 'kubernetes', 'certifications']
summary = 'A low-spec, homelab that can still run production-style Kubernetes and two of five exams down on the road to Kubestronaut.'
+++

This is the first real post on the site, so it's a status report: what's in the lab, what it's for, what it isn't doing yet, and where I am on the road to Kubestronaut.

TLDR: It's a small rack of mini PCs that cost less than the hobbiy gear I sold to pay for it, and  it still runs the same patterns I teach for production.

## Kubernetes at home

In 2019, I was a designer and architect teaching state of the art fabrication with 3D printing, CNC and laser cutting at the Academy of Art University in San Francisco. I loved the work, but I wanted to move into software, and as soon as I began developing in 2020, the world locked down.

- In 2021 I was hired to train engineers in cloud-native deployments on Kubernetes at a major telecom company.

- In 2022 I developed and taught CI/CD enabled deployments on GitLab with Terraform targeting AWS teams at a Fortune 50 insurance company.

- In 2024 I began training teams targeting deployments on ROSA (Red Hat OpenShift Service on AWS) with Argo CD and ESO on AWS Secret Manager.

Somewhere along the way I fell for distributed computing. It scratches the same itch architecture and industrial design did: systems made of standard parts, fitted together under constraints with real human users. The difference is the feedback loop. A building takes years to come to fruition while a cluster tells you within seconds whether you got it right. Plus, it's quite addicting to see pipelines go green.

I'd toyed with self-hosting for years, mostly as a way off streaming services and to keep up with ad blocking. What finally got me building, in 2025, was the next step in my career. I'm aiming to join a platform team in 2027, and I wanted somewhere to experiment that didn't result in a cloud bill, and something to show for it.

## The rack

The drawing on the front page of this site is an actual part of my homelab. Numbered from the bottom, the parts are:

1. `minovsky`, a **MikroTik CRS310-8G+2S+IN** managed switch running RouterOS.
2. A printed patch panel, with the switch's ports patched to it.
3. to 5. `zeta`, `mkii` and `rx78`: three **HP EliteDesk 800 G2 Minis**, each with a 2016-era **i5-6500T** and 16 GB of RAM.

The mini PCs were $70 each on eBay. They're quiet and they sip power. The switch was a bit of a splurge at $200. That's the whole cluster for about $400 plus a patch panel and some cables I patched myself.

Full specs can be found at [Current Hardware]({{< relref "/homelab/hardware" >}}).

Eventually, I'll post some photos of the rack. It is enclosed in a 3D printed white PETG **LabRax** case.

## What's actually running

Honestly? Not much yet, and that's on purpose.

The nodes run Arch Linux. I provisioned k3s across all three with Ansible, and the same playbooks bootstrap MetalLB for load balancer IPs and Argo CD for GitOps. The foundations for a production platform are there: the cluster is declared in code, apps come from Git, and services get real IPs on my network.

Arch and k3s were a teaching choice more than anything. Arch forces you understand every piece of the system because you install every piece yourself, and that forced me to actually learn Linux rather than rely on defaults from other distros. k3s let me get a working cluster up while I was preparing for the CKAD certification exam.

What I haven't done is put anything I depend on onto it. The cluster is my test bench, and it gets torn down pretty often. Self-hosting things my household relies on can wait until there's somewhere stable for them to live. I still have the CKA to prepare for which will require a rebuild of the cluster from scratch several times, and I want to get that done before I start putting anything important on it.

## Low Spec Tech

So far, the old hardware hasn't held me back yet. 16 GB of memory per node is plenty for a control plane, GitOps tooling and a handful of test workloads. Where I can see pains coming is in two places.

**Storage.** The missing piece is a NAS. I'm not a data hoarder. My film library is maybe thirty movies I like to rewatch and a few TV shows, plus save files for a few retro games I want synced between devices. My wife enjoys her streaming services, so those aren't going anywhere soon, but eventually I'd like to replace them with self-hosted alternatives. Even a small library needs a proper home, and the cluster's mini PCs aren't it yet.

**AI.** I want to run local models, and that means a GPU.

## The GPU problem

This is where I have been going round in circles.

The obvious candidate is `zz`, a custom build in a **Thermaltake Core V1** case with a **Ryzen 5 5500**, 32 GB of RAM and an **RTX 3060 12 GB** GPU. The card is a good fit for local AI at this level. Twelve gigabytes runs the common 7–8B models comfortably and a quantised 13–14B model at a pinch, plus speech-to-text and image generation. It's not going to run the big models, but it's plenty to learn on, including wiring a GPU into Kubernetes.

The problem is that `zz` has historically been my gaming PC, and I had trouble letting that go. I've tried. I bought handhelds to move my gaming onto. I even turned `zz` into a Linux box, but my wife and I play games together that need kernel-level anti-cheat, and unfortunately that means Windows.

Early this year I had a plan. The **HP Z2 G4 SFF** (`anaheim`), which I'd originally lined up as the NAS, would become the gaming PC with a low-profile **Radeon RX 6400** while `zz` would become an Ubuntu GPU node for local AI. But I got distracted with my gaming crew in the spring and never commited to the swap.

Some time soon, I'll make the switch so I can have a GPU enabled node for my cluster. I just have to stop flip-flopping long enough to do it.

## Low Spec Low Cost

I set myself one rule for the lab: don't spend more than I make selling the gear from previous hobbies. Cameras, bikes and gaming gear have all gone to fund it.

The [Hardware Timeline]({{< relref "/homelab/timeline" >}}) tracks everything since February 2025. It doesn't include all the gear I sold before that, but even so the trend is clear: I try not to spend too much out of pocket.

A lot of the lab is parts moving between machines and slow upgrades. If there's a real hobby hiding in here, it might be that. Now that the state of the lab is up on the site, I'm going to lock down the hardware for a while and focus on the software side.

## On the road to Kubestronaut

[Kubestronaut](https://www.cncf.io/training/kubestronaut/) is the CNCF's title for holding all five of its Kubernetes certifications: KCNA, KCSA, CKA, CKAD and CKS. I'm at two of five. The [Certifications]({{< relref "/homelab/certifications" >}}) page in my Homelab section has the full history, which goes back to an AWS Solutions Architect – Associate in 2021.

- **CKAD**, May 2025. The lab earned its keep here. Having a real multi-node cluster to break and fix made the exam's hands-on tasks feel routine.
- **KCNA**, February 2026.
- **CKA, CKS and KCSA** are still to go, covered by a four-exam bundle that expires in **March 2027**.

## What's next

- Rebuild the cluster from scratch for the CKA, then work through CKS and KCSA before March 2027.
- Finally make the switch: `anaheim` as the gaming PC, `zz` as a GPU node for local AI.

I'm pretty excited to keep everything tracked here on denhlab over in [Homelab]({{< relref "/homelab" >}}).
