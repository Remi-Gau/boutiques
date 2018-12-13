#!/usr/bin/env python

import os
from unittest import TestCase
import json
from boutiques import __file__ as bfile
import boutiques as bosh


class TestSimulate(TestCase):

    def get_examples_dir(self):
        return os.path.join(os.path.dirname(bfile),
                            "schema", "examples")

    def test_success(self):
        example1_dir = os.path.join(self.get_examples_dir(), "example1")
        self.assertFalse(bosh.execute("simulate",
                                      os.path.join(example1_dir,
                                                   "example1_docker.json"
                                                   )).exit_code)

        self.assertFalse(bosh.execute("simulate",
                                      os.path.join(self.get_examples_dir(),
                                                   "good_nooutputs.json"
                                                   )).exit_code)

    def test_success_desc_as_json_obj(self):
        example1_dir = os.path.join(self.get_examples_dir(), "example1")
        desc_json = open(os.path.join(example1_dir,
                                      "example1_docker.json")).read()
        self.assertFalse(bosh.execute("simulate",
                                      desc_json).exit_code)

        self.assertFalse(bosh.execute("simulate",
                                      os.path.join(self.get_examples_dir(),
                                                   "good_nooutputs.json"
                                                   )).exit_code)

    def test_success_desc_from_zenodo(self):
        self.assertFalse(bosh.execute("simulate",
                                      "zenodo.1472823").exit_code)

        self.assertFalse(bosh.execute("simulate",
                                      os.path.join(self.get_examples_dir(),
                                                   "good_nooutputs.json"
                                                   )).exit_code)

    def test_success_json(self):
        example1_dir = os.path.join(self.get_examples_dir(), "example1")
        desc_json = open(os.path.join(example1_dir,
                                      "example1_docker.json")).read()
        siminvo = bosh.execute("simulate", desc_json, "-j").stdout
        assert(isinstance(json.loads(siminvo), dict))
        siminvo = bosh.bosh(args=["example", desc_json]).stdout
        assert(isinstance(json.loads(siminvo), dict))

    def test_failing_bad_descriptor_invo_combos(self):
        example1_dir = os.path.join(self.get_examples_dir(), "example1")

        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(example1_dir,
                                                                  "fake.json"),
                                                     "-i",
                                                     os.path.join(
                                                       example1_dir,
                                                       "invocation.json")])
        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(
                                                       example1_dir,
                                                       "example1_docker.json"),
                                                     "-i",
                                                     os.path.join(example1_dir,
                                                                  "fake.json")])
        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(
                                                       example1_dir,
                                                       "example1_docker.json"),
                                                     "-i",
                                                     os.path.join(
                                                       example1_dir,
                                                       "exampleTool1.py")])
        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(
                                                       example1_dir,
                                                       "example1_docker.json")])
        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(
                                                       example1_dir,
                                                       "example1_docker.json"),
                                                     "-i",
                                                     os.path.join(
                                                       example1_dir,
                                                       "invocation.json")])
        self.assertRaises(SystemExit, bosh.execute, ["simulate",
                                                     os.path.join(
                                                       example1_dir,
                                                       "example1_docker.json")])
